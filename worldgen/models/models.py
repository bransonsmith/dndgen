from django.db import models
from django.utils import timezone

class TreasureHoardTier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    min_level = models.IntegerField(default=0)
    max_level = models.IntegerField(default=20)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return TreasureHoardTier(name=dict["name"], min_level=dict["min_level"], max_level=dict["max_level"])

class TreasureHoardRollTable(models.Model):
    tier = models.ForeignKey(TreasureHoardTier, on_delete=models.CASCADE)
    min_roll = models.IntegerField()
    max_roll = models.IntegerField()
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.min_roll}-{self.max_roll}) {self.tier.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        tier = TreasureHoardTier.objects.all().filter(name=dict["tier"]).first()
        return TreasureHoardRollTable(tier=tier, min_roll=dict["min_roll"], max_roll=dict["max_roll"])

class TreasureHoard(models.Model):
    tier = models.ForeignKey(TreasureHoardTier, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'

class ContentSource(models.Model):
    title = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.title}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return ContentSource(title=dict["title"], type=dict["type"], abbreviation=dict["abbreviation"])

class Rarity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(default=0)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return Rarity(name=dict["name"], order=dict["order"])


# Treasure Hoard Location Mapping
# Treasure Hoard Owner/Person/Monster Mapping

