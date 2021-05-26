from django.http import HttpResponse
from django.shortcuts import render
from ..models.location_models import *
import random
from.views import add, roll_dice, get_new_model_object

magical_locations = [
    { "roll_range": 10, "description": "", "name": "Hermit Hut" },
    { "roll_range":  5, "description": "", "name": "Wizard Tower" },
    { "roll_range":  3, "description": "", "name": "Arcane Forge" },
    { "roll_range":  2, "description": "", "name": "Enchanted Rune" },
    { "roll_range":  0, "description": "", "name": "Lich's Lair" },
    { "roll_range":  0, "description": "", "name": "Sorcerer's Stone" },
    { "roll_range":  0, "description": "", "name": "Portal" },
]

def roll_table(request, roll_table_name):
 
    roll_table_name = roll_table_name.title()    

    set_magical_locations_roll_table()

    try:
        roll_table = RollTable.objects.filter(name__iexact=roll_table_name).first()
        roll_table_entries = LocationRollTableEntry.objects.filter(roll_table=roll_table)

        all_locs = LocationType.objects.all()

        detailed_roll_table = {
            "name": roll_table.name,
            "rows": [],
            "total": 0
        }

        i = 1
        for entry in roll_table_entries:
            roll_entry = { "min": i, "max": i + entry.roll_quantity - 1, "text": entry.location_type.name }
            i += entry.roll_quantity
            detailed_roll_table["rows"].append(roll_entry)
        detailed_roll_table["total"] = i - 1

        context = { 
            "roll_table": detailed_roll_table,    
            "roll_table_name": roll_table_name,
            "all_locs": all_locs 
        }
        return render(request, 'roll_tables/index.html', context)
    except Exception as e:
        return HttpResponse(f'<h2>Error loading Roll Table: "{roll_table_name}"</h2><br><br><h3>{str(e)}</h3>')

def set_magical_locations_roll_table():
    LocationType.objects.all().delete()
    LocationRollTableEntry.objects.all().delete()
    RollTable.objects.all().delete()

    roll_table_obj = RollTable.get_model_from_seed_dict( { "name": "Magical Locations", "description" : "List of magical locations that could be in a world." } )
    roll_table_obj.save()

    for loc in magical_locations:
        loc_obj = LocationType.get_model_from_seed_dict(loc)
        loc_obj.save()

        if loc["roll_range"] > 0:
            loc_roll_obj = LocationRollTableEntry(roll_table=roll_table_obj, location_type=loc_obj, roll_quantity=loc["roll_range"])
            loc_roll_obj.save()