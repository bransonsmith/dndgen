from django.db.models.deletion import CASCADE
from .world_models import Environment
from django.db import models
from django.utils import timezone
from .roll_table_models import RollTable

class LocationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, default='')
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return LocationType(name=dict["name"], description=dict["description"])

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'

class LocationRollTableEntry(models.Model):
    roll_table = models.ForeignKey(RollTable, on_delete=models.CASCADE)
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    roll_quantity = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.roll_table.name} | {self.location_type.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        roll_table = RollTable.objects.filter(name__iexact=dict["roll_table"]).first()
        location_type = LocationType.objects.filter(name__iexact=dict["location_type"]).first()
        return LocationRollTableEntry(roll_table=roll_table, location_type=location_type, roll_quantity=dict["roll_quantity"])