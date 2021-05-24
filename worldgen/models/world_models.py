from django.db import models
from django.utils import timezone

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    height = models.IntegerField(default=1)
    width = models.IntegerField(default=1)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'

class EnvironmentType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return EnvironmentType(name=dict["name"])

class Environment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    environment_type = models.ForeignKey(EnvironmentType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    height = models.IntegerField(default=1)
    width = models.IntegerField(default=1)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'

class LocationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return LocationType(name=dict["name"])

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
