from django.db.models.base import Model
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from .models import ContentSource

class CreatureSize(models.Model):
    name = models.CharField(max_length=100, unique=True)
    space = models.DecimalField(default=0, max_digits=20, decimal_places=10)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return CreatureSize(name=dict["name"], space=dict["space"])

class MonsterType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return MonsterType(name=dict["name"], description=dict["description"])

class MonsterSubType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return MonsterSubType(name=dict["name"], description=dict["description"])

class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    playable = models.BooleanField(default=False)
    source = models.ForeignKey(ContentSource, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        source = ContentSource.objects.filter(title=dict["source"]).first() if dict["source"] is not None else None
        return Race(name=dict["name"], description=dict["description"], source=source, playable=dict["playable"])

class Monster(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cr = models.DecimalField(default=0, max_digits=20, decimal_places=10)
    monster_type = models.ForeignKey(MonsterType, on_delete=models.CASCADE)
    size = models.ForeignKey(CreatureSize, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True)
    subtype = models.ForeignKey(MonsterSubType, on_delete=models.CASCADE, null=True)
    is_legendary = models.BooleanField(default=False)
    ac =  models.IntegerField(default=0)
    hp =  models.IntegerField(default=0)
    source = models.ForeignKey(ContentSource, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        subtype = MonsterSubType.objects.filter(name__iexact=dict["subtype"]).first() if len(dict["subtype"]) > 0 else None
        race = Race.objects.filter(name__iexact=dict["race"]).first() if len(dict["race"]) > 0 else None
        monster_type = MonsterType.objects.filter(name__iexact=dict["monster_type"]).first()
        creature_size = CreatureSize.objects.filter(name__iexact=dict["size"]).first()
        source = ContentSource.objects.filter(title=dict["source"]).first()
        is_legendary = len(dict["isLegendary"]) > 0
        return Monster(name=dict["name"], cr=dict["cr"], monster_type=monster_type, size=creature_size, race=race, subtype=subtype, ac=dict["ac"], hp=dict["hp"], source=source, is_legendary=is_legendary) 

class EncounterDifficulty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return EncounterDifficulty(name=dict["name"]) 

class Encounter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    level = models.IntegerField(default=0)
    difficulty = models.ForeignKey(EncounterDifficulty, on_delete=models.CASCADE)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'

class MonsterInstance(models.Model):
    name = models.CharField(max_length=100, unique=True)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    current_hp = models.IntegerField(default=0)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name} | {self.monster}'

class EncounterXpThreshold(models.Model):
    level = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    difficulty = models.ForeignKey(EncounterDifficulty, on_delete=models.CASCADE)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.level} | {self.difficulty.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        difficulty = EncounterDifficulty.objects.filter(name__iexact=dict["difficulty"]).first()
        return EncounterXpThreshold(difficulty=difficulty, level=dict["level"], xp=dict["xp"]) 

class EncounterXpMultiplier(models.Model):
    monster_count_min = models.IntegerField(default=0)
    monster_count_max = models.IntegerField(default=0)
    multiplier = models.DecimalField(default=0, max_digits=20, decimal_places=10)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.monster_count_min}-{self.monster_count_max}) | {self.multiplier}x'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return EncounterXpMultiplier(monster_count_min=dict["monster_count_min"], monster_count_max=dict["monster_count_max"], multiplier=dict["multiplier"]) 

class CrXpValue(models.Model):
    cr = models.DecimalField(default=0, max_digits=20, decimal_places=10)
    xp = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.id} | {self.cr}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return CrXpValue(cr=dict["cr"], xp=dict["xp"]) 

# class Npc(models.Model):
#     name = models.CharField(max_length=100)
#     race = models.ForeignKey(Race, on_delete=models.CASCADE)
#     age = models.IntegerField(default=0)
#     gender = models.CharField(max_length=10, default='')
#     # talent
#     # good stat/bad stat etc.
#     created = models.DateTimeField('Creation Time', default=timezone.now)
#     def __str__(self):
#         return f'{self.id} | {self.name}'

# class Creature(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     ac =  models.IntegerField(default=0)
#     hp =  models.IntegerField(default=0)
#     # hit_dice = models.CharField(max_length=100, default='')
#     # speed =  models.IntegerField(default=0)
#     # swim_speed =  models.IntegerField(default=0)
#     # climb_speed = models.IntegerField(default=0)
#     # fly_speed = models.IntegerField(default=0)
#     # burrow_speed = models.IntegerField(default=0) 
#     created = models.DateTimeField('Creation Time', default=timezone.now)
#     def __str__(self):
#         return f'{self.id} | {self.name}'