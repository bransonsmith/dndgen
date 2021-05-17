from django.http import HttpResponse
from .models import  TreasureHoard, TreasureHoardTier, TreasureHoardRollTable, Rarity, ContentSource
from .art_object_models import ArtObject, ArtObjectGroup, ArtObjectGroupEntry, ArtObjectTreasureHoardEntry, TreasureHoardArtObjectRoll
from .gem_models import Gem, GemGroup, GemGroupEntry, GemTreasureHoardEntry, TreasureHoardGemRoll
from .coin_models import Coin, CoinTreasureHoardEntry, TreasureHoardCoinRoll
from .magic_item_models import ItemSignifigance, MagicItem, MagicItemGroup, MagicItemGroupEntry, MagicItemInstance, MagicItemTreasureHoardEntry, MagicItemType, TreasureHoardMagicItemRoll
import random
from .data.treasure_data import treasure_hoard_tiers, treasure_hoard_roll_tables, art_object_groups, gem_groups, rolls, art_object_group_entries, gem_group_entries, coins, raritys, content_sources, magic_items, magic_item_groups, magic_item_group_entries, magic_item_types, item_sigs

def index(request):
    outstr = '<style>body {color: #112244; background-color: #f5fdd9; width: 600px; display: flex; margin: auto; flex-direction: column;}</style>'

    # outstr += delete_all_treasure_hoard_data()
    # outstr += initiliaze_treasure_tables_to_dmg()
    outstr += create_sample_treasure_hoard(magic_item_group_entries, treasure_hoard_tiers)

    return HttpResponse(outstr)

def initiliaze_treasure_tables_to_dmg():
    outstr = '<br><br><b>Initiliazing Treasure Tables to DMG specifications.</b><br>'
    outstr += add(treasure_hoard_tiers, 'TreasureHoardTier')
    outstr += add(treasure_hoard_roll_tables, 'TreasureHoardRollTable')

    outstr += add(art_object_group_entries, 'ArtObject')
    outstr += add(art_object_groups, 'ArtObjectGroup')
    outstr += add(art_object_group_entries, 'ArtObjectGroupEntry')
    outstr += add(rolls, 'TreasureHoardArtObjectRoll')

    outstr += add(gem_group_entries, 'Gem')
    outstr += add(gem_groups, 'GemGroup')
    outstr += add(gem_group_entries, 'GemGroupEntry')
    outstr += add(rolls, 'TreasureHoardGemRoll')

    outstr += add(coins, 'Coin')
    outstr += addCoinRolls(rolls, 'TreasureHoardCoinRoll')

    outstr += add(raritys, 'Rarity')
    outstr += add(content_sources, 'ContentSource')
    outstr += add(item_sigs, 'ItemSignifigance')

    outstr += add(magic_item_types, 'MagicItemType')
    outstr += add(magic_item_groups, 'MagicItemGroup')

    outstr += addMagicItems(magic_items, magic_item_group_entries)
    outstr += add(magic_item_group_entries, 'MagicItemGroupEntry')
    outstr += addMagicItemRolls(rolls)
    return outstr

def create_sample_treasure_hoard(magic_item_group_entries, treasure_hoard_tiers):
    outstr = '<br><br><b>Creating Sample Treasure Hoard</b><br><br><br>'

    rand_tier_num = random.randint(0, len(treasure_hoard_tiers)-1)
    tier_name = treasure_hoard_tiers[rand_tier_num]["name"]

    tier = TreasureHoardTier.objects.filter(name__iexact=tier_name).first()
    th = TreasureHoard(tier=tier, name='Sample Treasure Hoard')
    th.save()

    roll_min = TreasureHoardRollTable.objects.all().order_by('min_roll').first().min_roll
    roll_max = TreasureHoardRollTable.objects.all().order_by('-max_roll').first().max_roll
    roll = random.randint(roll_min, roll_max)
    outstr = outstr + '<b>Rolling on treasure hoard table:' + str(tier.name) + ' <br>(' + str(roll_min) + '-' + str(roll_max) + ') => ' + str(roll) + '<br></b>'

    roll_table_result = TreasureHoardRollTable.objects.filter(tier=tier, min_roll__lte=roll, max_roll__gte=roll).first()

    art_object_rolls = TreasureHoardArtObjectRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    for art_roll in art_object_rolls:
        outstr = outstr + '<br><br>Need to add ' + str(art_roll.dice) + ' art objects from ' + str(art_roll.art_object_group.name)
        quantity = roll_dice(art_roll.dice)
        outstr = outstr + '<br>Quantity (' + art_roll.dice + ') => ' + str(quantity)

        art_object_group = art_roll.art_object_group
        art_min_roll = ArtObjectGroupEntry.objects.filter(art_object_group=art_object_group).order_by('min_roll').first().min_roll
        art_max_roll = ArtObjectGroupEntry.objects.filter(art_object_group=art_object_group).order_by('-max_roll').first().max_roll
        
        for i in range(0, quantity):
            art_die_roll = random.randint(art_min_roll, art_max_roll)
            # outstr = outstr + '<br>Art object table roll (' + str(art_min_roll) + '-' + str(art_max_roll) + ') => ' + str(art_die_roll)

            try:
                art_object = ArtObjectGroupEntry.objects.filter(art_object_group=art_object_group, min_roll__lte=art_die_roll, max_roll__gte=art_die_roll).first().art_object

                entry = ArtObjectTreasureHoardEntry(treasure_hoard=th, art_object=art_object, quantity=quantity)
                entry.save()
                outstr = outstr + '<br>' + '' + str(i + 1) + '. ' + str(entry.art_object.name)
            except Exception as e:
                outstr = outstr + '<br><b>' + str(i + 1) + '. FAILED! ' + str(e) + '</b>'

    gem_rolls = TreasureHoardGemRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    for gem_roll in gem_rolls:
        outstr = outstr + '<br><br>Need to add ' + str(gem_roll.dice) + ' gems from ' + str(gem_roll.gem_group.name)
        quantity = roll_dice(gem_roll.dice)
        outstr = outstr + '<br>Quantity (' + gem_roll.dice + ') => ' + str(quantity)

        gem_group = gem_roll.gem_group
        gem_min_roll = GemGroupEntry.objects.filter(gem_group=gem_group).order_by('min_roll').first().min_roll
        gem_max_roll = GemGroupEntry.objects.filter(gem_group=gem_group).order_by('-max_roll').first().max_roll
        
        for i in range(0, quantity):
            gem_die_roll = random.randint(gem_min_roll, gem_max_roll)
            # outstr = outstr + '<br>Gem table roll (' + str(gem_min_roll) + '-' + str(gem_max_roll) + ') => ' + str(gem_die_roll)

            gem = GemGroupEntry.objects.filter(gem_group=gem_group, min_roll__lte=gem_die_roll, max_roll__gte=gem_die_roll).first().gem

            try:
                entry = GemTreasureHoardEntry(treasure_hoard=th, gem=gem, quantity=quantity)
                entry.save()
                outstr = outstr + '<br>' + '' + str(i + 1) + '. ' + str(entry.gem.name)
            except Exception as e:
                outstr = outstr + '<br><b>' + str(i + 1) + '. FAILED! ' + str(e) + '</b>'

    coin_rolls = TreasureHoardCoinRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    for coin_roll in coin_rolls:
        outstr = outstr + '<br><br>Need to add ' + str(coin_roll.dice) + ' ' + str(coin_roll.coin.abbreviation)
        quantity = roll_dice(coin_roll.dice)
        # outstr = outstr + '<br>Quantity (' + coin_roll.dice + ') => ' + str(quantity)

        entry = CoinTreasureHoardEntry(treasure_hoard=th, coin=coin_roll.coin, quantity=quantity)
        entry.save()
        outstr = outstr + '<br>' + str(quantity) + ' ' + str(entry.coin.abbreviation)

    magic_rolls = TreasureHoardMagicItemRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    for magic_roll in magic_rolls:
        outstr = outstr + '<br><br>Need to add ' + str(magic_roll.dice) + ' items from ' + str(magic_roll.magic_item_group.name)
        quantity = roll_dice(magic_roll.dice)
        outstr = outstr + '<br>Quantity (' + magic_roll.dice + ') => ' + str(quantity)

        magic_item_group = magic_roll.magic_item_group
        magic_item_min_roll = MagicItemGroupEntry.objects.filter(magic_item_group=magic_item_group).order_by('min_roll').first().min_roll
        magic_item_max_roll = MagicItemGroupEntry.objects.filter(magic_item_group=magic_item_group).order_by('-max_roll').first().max_roll
        
        for i in range(0, quantity):
            magic_item_die_roll = random.randint(magic_item_min_roll, magic_item_max_roll)
            # outstr = outstr + '<br>Magic Item table roll (' + str(magic_item_min_roll) + '-' + str(magic_item_max_roll) + ') => ' + str(magic_item_die_roll)
            try:
                magic_item_entry = MagicItemGroupEntry.objects.filter(magic_item_group=magic_item_group, min_roll__lte=magic_item_die_roll, max_roll__gte=magic_item_die_roll).first()
                magic_item = magic_item_entry.magic_item

                if len(magic_item_entry.extra_dice) > 0:
                    extra_roll = roll_dice(magic_item_entry.extra_dice)
                    extra_group = MagicItemGroup.objects.filter(name=magic_item_entry.extra_group.name).first()
                    magic_item = MagicItemGroupEntry.objects.filter(magic_item_group=extra_group, min_roll__lte=extra_roll, max_roll__gte=extra_roll).first().magic_item
        
                magic_item_instance = MagicItemInstance(name=magic_item.name, magic_item=magic_item)
                magic_item_instance.save()

                entry = MagicItemTreasureHoardEntry(treasure_hoard=th, magic_item_instance=magic_item_instance, quantity=quantity)
                entry.save()
                outstr = outstr + '<br>' + str(i + 1) + '. ' + str(entry.magic_item_instance.name)
            except Exception as e:
                outstr = outstr + '<b><br>' + str(i + 1) + '. FAILED! ' + str(e)

    return outstr

def delete_all_treasure_hoard_data():
    outstr = 'Deleting data from all treasure tables<br><br>'
    TreasureHoard.objects.all().delete()
    TreasureHoardTier.objects.all().delete()
    TreasureHoardRollTable.objects.all().delete()
    Rarity.objects.all().delete()
    ContentSource.objects.all().delete()
    ArtObject.objects.all().delete()
    ArtObjectGroup.objects.all().delete()
    ArtObjectGroupEntry.objects.all().delete()
    ArtObjectTreasureHoardEntry.objects.all().delete()
    TreasureHoardArtObjectRoll.objects.all().delete()
    Gem.objects.all().delete()
    GemGroup.objects.all().delete()
    GemGroupEntry.objects.all().delete()
    GemTreasureHoardEntry.objects.all().delete()
    TreasureHoardGemRoll.objects.all().delete()
    Coin.objects.all().delete()
    CoinTreasureHoardEntry.objects.all().delete()
    TreasureHoardCoinRoll.objects.all().delete()
    ItemSignifigance.objects.all().delete()
    MagicItem.objects.all().delete()
    MagicItemGroup.objects.all().delete()
    MagicItemGroupEntry.objects.all().delete()
    MagicItemInstance.objects.all().delete()
    MagicItemTreasureHoardEntry.objects.all().delete()
    MagicItemType.objects.all().delete()
    TreasureHoardMagicItemRoll.objects.all().delete()
    return outstr

def addCoinRolls(objects, model_type:str):
    outstr = '<br><br><b>Adding many ' + model_type + 's</b><br>'
    count = 0
    for obj in objects:
        i = 0
        for coin_roll in obj['coin_rolls']:
            count = count + 1
            obj['coin_dice'] = coin_roll
            obj['coin_brev'] = obj["coin_values"][i]
            try:
                new_object = get_new_model_object(model_type, obj)
                if new_object is not None:
                    new_object.save()
                    outstr = outstr + ' ' + str(count).rjust(4) + '. created |' + str(new_object) + ' <br>'
            except Exception as error:
                outstr = outstr + ' ' + str(count).rjust(4) + '. FAILED! |' + str(obj) + ' <br> <b>' + str(error) + '</b><br>'
            i = i + 1
    return outstr

def addMagicItems(magic_items, magic_item_group_entries):
    outstr = '<br><b>Adding Magic Items</b><br>'

    for magic_item in magic_items:
        group_entries = list(filter(lambda x: x["item_name"] == magic_item["name"], magic_item_group_entries))
        sig = "Unknown"
        if len(group_entries) > 0:
            sig = group_entries[0]["signifigance"]
        description = ""
        magic_item_type = MagicItemType.objects.filter(name=magic_item["magic_item_type"]).first()
        rarity = Rarity.objects.filter(name=magic_item["rarity"]).first()
        attunement = (len(magic_item["attunement"]) > 0)
        signifigance = ItemSignifigance.objects.filter(name=sig).first()
        source = ContentSource.objects.filter(title=magic_item["source"]).first()     
        
        try:
            new_object = MagicItem(name=magic_item["name"], magic_item_type=magic_item_type, rarity=rarity, attunement=attunement, signifigance=signifigance, source=source, description=description)  
            if new_object is not None:
                new_object.save()
                outstr = outstr + ' ' + '. created |' + str(new_object) + ' <br>'
        except Exception as error:
            outstr = outstr + ' ' + '. FAILED! |' + str(magic_item) + ' <br> <b>' + str(error) + '</b><br>'

    return outstr

def addMagicItemRolls(rolls):
    outstr = '<br><br><b>Adding Many Magic Item Rolls</b><br>'
    count = 0
    for roll in rolls:
        i = 0
        for magic_roll in roll['magic_item_rolls']:
            count = count + 1
            roll['magic_dice'] = magic_roll
            roll['magic_group'] = roll["magic_item_groups"][i]
            try:
                new_object = get_new_model_object('TreasureHoardMagicItemRoll', roll)
                if new_object is not None:
                    new_object.save()
                    outstr = outstr + ' ' + str(count).rjust(4) + '. created |' + str(new_object) + ' <br>'
            except Exception as error:
                outstr = outstr + ' ' + str(count).rjust(4) + '. FAILED! |' + str(roll) + ' <br> <b>' + str(error) + '</b><br>'
            i = i + 1
    return outstr

def add(objects, model_type:str):
    outstr = '<br><br><b>Adding ' + str(len(objects)) + ' ' + model_type + 's</b><br>'
    count = 0
    for obj in objects:
        count = count + 1
        try:
            new_object = get_new_model_object(model_type, obj)
            if new_object is not None:
                new_object.save()
                outstr = outstr + ' ' + str(count).rjust(4) + '. created |' + str(new_object) + ' <br>'
        except Exception as error:
            outstr = outstr + ' ' + str(count).rjust(4) + '. FAILED! |' + str(obj) + ' <br> <b>' + str(error) + '</b><br>'
    return outstr

def get_new_model_object(model_type, dict):
    try:
        return globals()[model_type].get_model_from_seed_dict(dict)
    except Exception as e:
        raise Exception('Model Type Not Found: ' + model_type)

def roll_dice(dice: str):
    dice_split = dice.split('d')
    if len(dice_split) == 1:
        pre = 1
    else:
        pre = int(dice.split('d')[0])
    
    post = int(dice_split[-1])

    total = 0
    for i in range(0, pre):
        total = total + random.randint(1, post)
    return total