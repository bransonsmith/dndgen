import math
from django.http import HttpResponse
from ..models.models import Rarity, ContentSource
from ..models.monster_models import *
import random
import math
from ..data.monster_data import *
from ..data.creature_data import creature_sizes, races
from ..data.treasure_data import raritys, content_sources
from.views import add, roll_dice, get_new_model_object

def monster(request):
    outstr = '<style>body {color: #112244; background-color: #f5fdd9; width: 600px; display: flex; margin: auto; flex-direction: column;}</style>'
    outstr = '<h1>Monsters</h1>'
    outstr += delete_all_monster_data()
    outstr += initiliaze_monster_tables_to_dmg()
    outstr += create_sample_monster_encounter()

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
    outstr += add(encounter_difficulties, 'EncounterDifficulty')
    outstr += add(encounter_multipliers, 'EncounterXpMultiplier')
    outstr += add(encounter_thresholds, 'EncounterXpThreshold')
    outstr += add(cr_xp, 'CrXpValue')
    return outstr

def create_sample_monster_encounter():
    outstr = '<br><br><b>Creating Sample Monster Encounter</b><br><br><br>'

    party_level = random.randint(1, 10)
    num_players = random.randint(3, 5)
    dif_index = random.randint(0, len(encounter_difficulties) -1)
    difficulty = encounter_difficulties[dif_index]["name"]
    budget = EncounterXpThreshold.objects.filter(level=party_level, difficulty__name__contains=difficulty).first().xp * num_players

    outstr += '<br>Party Level: ' + str(party_level)
    outstr += '<br>Party Size: ' + str(num_players)
    outstr += '<br>Difficulty: ' + str(difficulty)
    outstr += '<br>Total XP Budget: ' + str(budget)

    outstr += '<br><br>Getting monsters from: "All Monsters, Equally Weighted"'

    all_monsters = Monster.objects.all()
    monster_count = len(all_monsters)
    outstr += '<br>Selecting from ' + str(monster_count) + ' monsters...'

    budget_left = budget
    selected_monster = None
    num_monsters = 0
    while budget_left > 49:
        while selected_monster is None:
            monster_index = random.randint(0, len(all_monsters) -1)
            mon = list(all_monsters)[monster_index]
            xp = CrXpValue.objects.filter(cr=mon.cr).first().xp
            if xp < budget_left:
                selected_monster = mon
                num_monsters = random.randint(1, math.floor(budget_left / xp))
                budget_left -= xp * num_monsters
        outstr += '<br>Adding ' + str(num_monsters) + 'x ' + str(selected_monster.name)+ ' cr = ' + str(round(selected_monster.cr, 3)) + ' (-' + str(xp * num_monsters) + 'xp)'
        selected_monster = None

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
    EncounterDifficulty.objects.all().delete()
    EncounterXpMultiplier.objects.all().delete()
    EncounterXpThreshold.objects.all().delete()
    CrXpValue.objects.all().delete()
    return outstr
