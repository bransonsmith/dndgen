from django.http import HttpResponse
from django.shortcuts import render
from ..models.location_models import *
from django.shortcuts import render
from rest_framework import viewsets
from ..serializers.roll_table_serializers import *

class RollTableViewSet(viewsets.ModelViewSet):
    serializer_class = RollTableSerializer
    queryset = RollTable.objects.all()
    lookup_field = 'name'

class LocationRollTableEntryViewSet(viewsets.ModelViewSet):
    serializer_class = LocationRollTableEntrySerializer
    queryset = LocationRollTableEntry.objects.all()

class LocationTypeViewSet(viewsets.ModelViewSet):
    serializer_class = LocationTypeSerializer
    queryset = LocationType.objects.all()
    lookup_field = 'name'

magical_locations = [
    { "roll_range": 10, "description": "", "name": "Hermit Hut" },
    { "roll_range":  5, "description": "", "name": "Wizard Tower" },
    { "roll_range":  3, "description": "", "name": "Arcane Forge" },
    { "roll_range":  2, "description": "", "name": "Enchanted Rune" },
    { "roll_range":  1, "description": "", "name": "Lich's Lair" },
    { "roll_range":  2, "description": "", "name": "Sorcerer's Stone" },
    { "roll_range":  4, "description": "", "name": "Portal" },
]

settlement_locations = [
    { "roll_range":  2, "description": "", "name": "City" },
    { "roll_range":  5, "description": "", "name": "Town" },
    { "roll_range":  3, "description": "", "name": "Settlement" },
    { "roll_range":  1, "description": "", "name": "Commune" },
    { "roll_range":  5, "description": "", "name": "Lord's Demesne" },
    { "roll_range":  2, "description": "", "name": "Estate" },
    { "roll_range":  1, "description": "", "name": "Shire" },
]

def generate_roll_tables(request):
    outstr = '<h1>Generating Roll Tables</h1>'   

    outstr += delete_location_data()
    outstr += set_magical_locations_roll_table()
    outstr += set_settlement_locations_roll_table()

    return HttpResponse(outstr)

def set_magical_locations_roll_table():
    roll_table_obj = RollTable.get_model_from_seed_dict( { "name": "Magical Locations", "description" : "List of magical locations that could be in a world." } )
    roll_table_obj.save()

    order = 0
    for loc in magical_locations:
        loc_obj = LocationType.get_model_from_seed_dict(loc)
        loc_obj.save()

        if loc["roll_range"] > 0:
            order = order + 1
            loc_roll_obj = LocationRollTableEntry(order=order, roll_table=roll_table_obj, location_type=loc_obj, roll_quantity=loc["roll_range"])
            loc_roll_obj.save()
    return '<br><h3>Added Magical Locations Roll Table</h3>'

def set_settlement_locations_roll_table():
    roll_table_obj = RollTable.get_model_from_seed_dict( { "name": "Settlement Locations", "description" : "List of settlement locations that could be in a world." } )
    roll_table_obj.save()

    order = 0
    for loc in settlement_locations:
        loc_obj = LocationType.get_model_from_seed_dict(loc)
        loc_obj.save()

        if loc["roll_range"] > 0:
            order = order + 1
            loc_roll_obj = LocationRollTableEntry(order=order, roll_table=roll_table_obj, location_type=loc_obj, roll_quantity=loc["roll_range"])
            loc_roll_obj.save()
    return '<br><h3>Added Settlement Locations Roll Table</h3>'

def delete_location_data():
    LocationType.objects.all().delete()
    LocationRollTableEntry.objects.all().delete() 
    RollTable.objects.all().delete()

    return '<br><h3>Deleted Roll Table Data.</h3>'
