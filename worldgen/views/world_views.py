import math
from django.http import HttpResponse
from ..models.models import Rarity, ContentSource
from ..models.monster_models import *
import random
import math
from ..data.world_data import *
from ..models.world_models import *
from.views import add, roll_dice, get_new_model_object

def world(request):
    outstr = '<style>body {color: #112244; background-color: #f5fdd9; width: 600px; display: flex; margin: auto; flex-direction: column;}</style>'
    outstr = '<h1>World</h1>'
    outstr += delete_all_world_data()
    outstr += initiliaze_world_tables()
    outstr += create_sample_region()

    return HttpResponse(outstr)

def initiliaze_world_tables():
    outstr = '<br><br><b>Initiliazing Region Tables.</b><br>'
    outstr += add(environment_types, 'EnvironmentType')
    outstr += add(location_types, 'LocationType')
    
    return outstr

def create_sample_region():
    outstr = '<br><br><b>Creating Sample Region</b><br>'

    region = Region(name="Sample Region", description="A simple example region.", height=1, width=1, x=0, y=0)
    region.save()

    rand_name = environment_types[random.randint(0, len(environment_types) - 1)]['name']
    environment_type = EnvironmentType.objects.filter(name=rand_name).first()
    env_name = "The Great Test " + environment_type.name
    environment = Environment(name=env_name, description="some test env", environment_type=environment_type, region=region, height=2, width=2, x=0, y=0)
    environment.save()
    
    rand_name = location_types[random.randint(0, len(location_types) - 1)]['name']
    location_a_type = LocationType.objects.filter(name=rand_name).first()
    loc_name = location_a_type.name + " Loc A"
    location_a = Location(name=loc_name, description="Sample location a", environment=environment, location_type=location_a_type, height=1, width=1, x=0, y=0)
    location_a.save()
    
    rand_name = location_types[random.randint(0, len(location_types) - 1)]['name']
    location_b_type = LocationType.objects.filter(name=rand_name).first()
    loc_name = location_b_type.name + " Loc B"
    location_b = Location(name=loc_name, description="Sample location b", environment=environment, location_type=location_b_type, height=1, width=1, x=1, y=0)
    location_b.save()
    
    rand_name = location_types[random.randint(0, len(location_types) - 1)]['name']
    location_c_type = LocationType.objects.filter(name=rand_name).first()
    loc_name = location_c_type.name + " Loc C"
    location_c = Location(name=loc_name, description="Sample location c", environment=environment, location_type=location_c_type, height=1, width=1, x=0, y=1)
    location_c.save()
    
    rand_name = location_types[random.randint(0, len(location_types) - 1)]['name']
    location_d_type = LocationType.objects.filter(name=rand_name).first()
    loc_name = location_d_type.name + " Loc D"
    location_d = Location(name=loc_name, description="Sample location d", environment=environment, location_type=location_d_type, height=1, width=1, x=1, y=1)
    location_d.save()

    outstr += '<br>Region = ' + str(region)
    outstr += '<br>Environment = ' + str(environment)
    outstr += '<br>Location A = ' + str(location_a)
    outstr += '<br>Location B = ' + str(location_b)
    outstr += '<br>Location C = ' + str(location_c)
    outstr += '<br>Location D = ' + str(location_d)

    return outstr

def delete_all_world_data():
    outstr = 'Deleting data from all world tables<br><br>'
    Region.objects.all().delete()
    Location.objects.all().delete()
    Environment.objects.all().delete()
    EnvironmentType.objects.all().delete()
    LocationType.objects.all().delete()

    return outstr
