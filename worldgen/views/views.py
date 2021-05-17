from django.http import HttpResponse
def index(request):
    outstr = '<style>body {color: #112244; background-color: #f5fdd9; width: 600px; display: flex; margin: auto; flex-direction: column;}</style>'
    outstr += 'World Gen Home'
    return HttpResponse(outstr)
import random

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