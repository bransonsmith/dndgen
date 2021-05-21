from django.http import HttpResponse
from ..models.models import Rarity, ContentSource
from ..models.monster_models import *
import random
from ..data.monster_data import monster_types, monsters, subtypes
from ..data.creature_data import creature_sizes, races
from ..data.treasure_data import raritys, content_sources
from.views import add, roll_dice, get_new_model_object

def monster(request):
    outstr = '<style>body {color: #112244; background-color: #f5fdd9; width: 600px; display: flex; margin: auto; flex-direction: column;}</style>'
    outstr = '<h1>Monsters</h1>'
    outstr += delete_all_monster_data()
    outstr += initiliaze_monster_tables_to_dmg()
    # outstr += create_sample_treasure_hoard(magic_item_group_entries, treasure_hoard_tiers)

    return HttpResponse(outstr)

def initiliaze_monster_tables_to_dmg():
    outstr = '<br><br><b>Initiliazing Monster Tables to DMG specifications.</b><br>'
    outstr += add(raritys, 'Rarity')
    outstr += add(content_sources, 'ContentSource')
    outstr += add(creature_sizes, 'CreatureSize')
    outstr += add(monster_types, 'MonsterType')
    outstr += add(subtypes, 'MonsterSubType')
    outstr += add(races, 'Race')
    outstr += add(monsters, 'Monster')
    return outstr

def create_sample_treasure_hoard(magic_item_group_entries, treasure_hoard_tiers):
    outstr = '<br><br><b>Creating Sample Treasure Hoard</b><br><br><br>'

    # rand_tier_num = random.randint(0, len(treasure_hoard_tiers)-1)
    # tier_name = treasure_hoard_tiers[rand_tier_num]["name"]

    # tier = TreasureHoardTier.objects.filter(name__iexact=tier_name).first()
    # th = TreasureHoard(tier=tier, name='Sample Treasure Hoard')
    # th.save()

    # roll_min = TreasureHoardRollTable.objects.all().order_by('min_roll').first().min_roll
    # roll_max = TreasureHoardRollTable.objects.all().order_by('-max_roll').first().max_roll
    # roll = random.randint(roll_min, roll_max)
    # outstr = outstr + '<b>Rolling on treasure hoard table:' + str(tier.name) + ' <br>(' + str(roll_min) + '-' + str(roll_max) + ') => ' + str(roll) + '<br></b>'

    # roll_table_result = TreasureHoardRollTable.objects.filter(tier=tier, min_roll__lte=roll, max_roll__gte=roll).first()

    # art_object_rolls = TreasureHoardArtObjectRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    # for art_roll in art_object_rolls:
    #     outstr = outstr + '<br><br>Need to add ' + str(art_roll.dice) + ' art objects from ' + str(art_roll.art_object_group.name)
    #     quantity = roll_dice(art_roll.dice)
    #     outstr = outstr + '<br>Quantity (' + art_roll.dice + ') => ' + str(quantity)

    #     art_object_group = art_roll.art_object_group
    #     art_min_roll = ArtObjectGroupEntry.objects.filter(art_object_group=art_object_group).order_by('min_roll').first().min_roll
    #     art_max_roll = ArtObjectGroupEntry.objects.filter(art_object_group=art_object_group).order_by('-max_roll').first().max_roll
        
    #     for i in range(0, quantity):
    #         art_die_roll = random.randint(art_min_roll, art_max_roll)
    #         # outstr = outstr + '<br>Art object table roll (' + str(art_min_roll) + '-' + str(art_max_roll) + ') => ' + str(art_die_roll)

    #         try:
    #             art_object = ArtObjectGroupEntry.objects.filter(art_object_group=art_object_group, min_roll__lte=art_die_roll, max_roll__gte=art_die_roll).first().art_object

    #             entry = ArtObjectTreasureHoardEntry(treasure_hoard=th, art_object=art_object, quantity=quantity)
    #             entry.save()
    #             outstr = outstr + '<br>' + '' + str(i + 1) + '. ' + str(entry.art_object.name)
    #         except Exception as e:
    #             outstr = outstr + '<br><b>' + str(i + 1) + '. FAILED! ' + str(e) + '</b>'

    # gem_rolls = TreasureHoardGemRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    # for gem_roll in gem_rolls:
    #     outstr = outstr + '<br><br>Need to add ' + str(gem_roll.dice) + ' gems from ' + str(gem_roll.gem_group.name)
    #     quantity = roll_dice(gem_roll.dice)
    #     outstr = outstr + '<br>Quantity (' + gem_roll.dice + ') => ' + str(quantity)

    #     gem_group = gem_roll.gem_group
    #     gem_min_roll = GemGroupEntry.objects.filter(gem_group=gem_group).order_by('min_roll').first().min_roll
    #     gem_max_roll = GemGroupEntry.objects.filter(gem_group=gem_group).order_by('-max_roll').first().max_roll
        
    #     for i in range(0, quantity):
    #         gem_die_roll = random.randint(gem_min_roll, gem_max_roll)
    #         # outstr = outstr + '<br>Gem table roll (' + str(gem_min_roll) + '-' + str(gem_max_roll) + ') => ' + str(gem_die_roll)

    #         gem = GemGroupEntry.objects.filter(gem_group=gem_group, min_roll__lte=gem_die_roll, max_roll__gte=gem_die_roll).first().gem

    #         try:
    #             entry = GemTreasureHoardEntry(treasure_hoard=th, gem=gem, quantity=quantity)
    #             entry.save()
    #             outstr = outstr + '<br>' + '' + str(i + 1) + '. ' + str(entry.gem.name)
    #         except Exception as e:
    #             outstr = outstr + '<br><b>' + str(i + 1) + '. FAILED! ' + str(e) + '</b>'

    # coin_rolls = TreasureHoardCoinRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    # for coin_roll in coin_rolls:
    #     outstr = outstr + '<br><br>Need to add ' + str(coin_roll.dice) + ' ' + str(coin_roll.coin.abbreviation)
    #     quantity = roll_dice(coin_roll.dice)
    #     # outstr = outstr + '<br>Quantity (' + coin_roll.dice + ') => ' + str(quantity)

    #     entry = CoinTreasureHoardEntry(treasure_hoard=th, coin=coin_roll.coin, quantity=quantity)
    #     entry.save()
    #     outstr = outstr + '<br>' + str(quantity) + ' ' + str(entry.coin.abbreviation)

    # magic_rolls = TreasureHoardMagicItemRoll.objects.filter(treasure_hoard_roll=roll_table_result)
    # for magic_roll in magic_rolls:
    #     outstr = outstr + '<br><br>Need to add ' + str(magic_roll.dice) + ' items from ' + str(magic_roll.magic_item_group.name)
    #     quantity = roll_dice(magic_roll.dice)
    #     outstr = outstr + '<br>Quantity (' + magic_roll.dice + ') => ' + str(quantity)

    #     magic_item_group = magic_roll.magic_item_group
    #     magic_item_min_roll = MagicItemGroupEntry.objects.filter(magic_item_group=magic_item_group).order_by('min_roll').first().min_roll
    #     magic_item_max_roll = MagicItemGroupEntry.objects.filter(magic_item_group=magic_item_group).order_by('-max_roll').first().max_roll
        
    #     for i in range(0, quantity):
    #         magic_item_die_roll = random.randint(magic_item_min_roll, magic_item_max_roll)
    #         # outstr = outstr + '<br>Magic Item table roll (' + str(magic_item_min_roll) + '-' + str(magic_item_max_roll) + ') => ' + str(magic_item_die_roll)
    #         try:
    #             magic_item_entry = MagicItemGroupEntry.objects.filter(magic_item_group=magic_item_group, min_roll__lte=magic_item_die_roll, max_roll__gte=magic_item_die_roll).first()
    #             magic_item = magic_item_entry.magic_item

    #             if len(magic_item_entry.extra_dice) > 0:
    #                 extra_roll = roll_dice(magic_item_entry.extra_dice)
    #                 extra_group = MagicItemGroup.objects.filter(name=magic_item_entry.extra_group.name).first()
    #                 magic_item = MagicItemGroupEntry.objects.filter(magic_item_group=extra_group, min_roll__lte=extra_roll, max_roll__gte=extra_roll).first().magic_item
        
    #             magic_item_instance = MagicItemInstance(name=magic_item.name, magic_item=magic_item)
    #             magic_item_instance.save()

    #             entry = MagicItemTreasureHoardEntry(treasure_hoard=th, magic_item_instance=magic_item_instance, quantity=quantity)
    #             entry.save()
    #             outstr = outstr + '<br>' + str(i + 1) + '. ' + str(entry.magic_item_instance.name)
    #         except Exception as e:
    #             outstr = outstr + '<b><br>' + str(i + 1) + '. FAILED! ' + str(e)

    return outstr

def delete_all_monster_data():
    outstr = 'Deleting data from all monster tables<br><br>'
    Rarity.objects.all().delete()
    ContentSource.objects.all().delete()
    CreatureSize.objects.all().delete()
    MonsterType.objects.all().delete()
    MonsterSubType.objects.all().delete()
    Monster.objects.all().delete()
    Race.objects.all().delete()
    return outstr
