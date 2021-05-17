from .models import TreasureHoard, TreasureHoardRollTable, TreasureHoardTier
from django.db import models
from django.utils import timezone

class Gem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, default='')
    value = models.IntegerField(default=10)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return Gem(name=dict["gem"], value=dict["value"], description=dict["gem_desc"])

class GemGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return GemGroup(name=dict["name"], description=dict["description"])

class GemGroupEntry(models.Model):
    gem = models.ForeignKey(Gem, on_delete=models.CASCADE)
    gem_group = models.ForeignKey(GemGroup, on_delete=models.CASCADE)
    min_roll = models.IntegerField()
    max_roll = models.IntegerField()
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.min_roll}-{self.max_roll}) {self.gem.name} > {self.gem_group.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        gem_group = GemGroup.objects.all().filter(name=dict["gem_group"]).first()
        gem = Gem.objects.all().filter(name=dict["gem"]).first()
        return GemGroupEntry(gem=gem, gem_group=gem_group, min_roll=dict["min_roll"], max_roll=dict["max_roll"])

# Ex: a roll on a hoard table would give 2d4 objects from group X
class TreasureHoardGemRoll(models.Model):
    treasure_hoard_roll = models.ForeignKey(TreasureHoardRollTable, on_delete=models.CASCADE)
    dice = models.CharField(max_length=100)
    gem_group = models.ForeignKey(GemGroup, on_delete=models.CASCADE)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.treasure_hoard_roll.min_roll}-{self.treasure_hoard_roll.max_roll}) {self.dice} {self.gem_group.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        if dict["gem_group"] != "":
            tier = TreasureHoardTier.objects.all().filter(name=dict["tier"]).first()
            treasure_hoard_roll = TreasureHoardRollTable.objects.all().filter(tier=tier, min_roll=dict["min_roll"], max_roll=dict["max_roll"]).first()            
            gem_group = GemGroup.objects.all().filter(name=dict["gem_group"]).first()            
            dice = dict["dice"]
            return TreasureHoardGemRoll(treasure_hoard_roll=treasure_hoard_roll, dice=dice, gem_group=gem_group)
        return None

class GemTreasureHoardEntry(models.Model):
    treasure_hoard = models.ForeignKey(TreasureHoard, on_delete=models.CASCADE)
    gem = models.ForeignKey(Gem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.quantity} {self.gem.name} in {self.treasure_hoard.name}'
