from .models import TreasureHoard, TreasureHoardRollTable, TreasureHoardTier
from django.db import models
from django.utils import timezone

class ArtObject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField(default=10)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return ArtObject(name=dict["art_object"], value=dict["value"])

class ArtObjectGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return ArtObjectGroup(name=dict["name"], description=dict["description"])

class ArtObjectGroupEntry(models.Model):
    art_object = models.ForeignKey(ArtObject, on_delete=models.CASCADE)
    art_object_group = models.ForeignKey(ArtObjectGroup, on_delete=models.CASCADE)
    min_roll = models.IntegerField()
    max_roll = models.IntegerField()
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.min_roll}-{self.max_roll}) {self.art_object.name} > {self.art_object_group.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        art_object_group = ArtObjectGroup.objects.all().filter(name=dict["art_object_group"]).first()
        art_object = ArtObject.objects.all().filter(name=dict["art_object"]).first()
        return ArtObjectGroupEntry(art_object=art_object, art_object_group=art_object_group, min_roll=dict["min_roll"], max_roll=dict["max_roll"])

# Ex: a roll on a hoard table would give 2d4 objects from group X
class TreasureHoardArtObjectRoll(models.Model):
    treasure_hoard_roll = models.ForeignKey(TreasureHoardRollTable, on_delete=models.CASCADE)
    dice = models.CharField(max_length=100)
    art_object_group = models.ForeignKey(ArtObjectGroup, on_delete=models.CASCADE)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.treasure_hoard_roll.min_roll}-{self.treasure_hoard_roll.max_roll}) {self.dice} {self.art_object_group.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        if dict["art_group"] != "":
            tier = TreasureHoardTier.objects.all().filter(name=dict["tier"]).first()
            treasure_hoard_roll = TreasureHoardRollTable.objects.all().filter(tier=tier, min_roll=dict["min_roll"], max_roll=dict["max_roll"]).first()            
            art_object_group = ArtObjectGroup.objects.all().filter(name=dict["art_group"]).first()            
            dice = dict["dice"]
            return TreasureHoardArtObjectRoll(treasure_hoard_roll=treasure_hoard_roll, dice=dice, art_object_group=art_object_group)
        return None

class ArtObjectTreasureHoardEntry(models.Model):
    treasure_hoard = models.ForeignKey(TreasureHoard, on_delete=models.CASCADE)
    art_object = models.ForeignKey(ArtObject, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.quantity} {self.art_object.name} in {self.treasure_hoard.name}'
