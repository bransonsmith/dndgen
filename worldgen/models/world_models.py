from django.db import models
from django.utils import timezone

# class Region(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.CharField(max_length=500)
#     height = models.IntegerField(default=1)
#     width = models.IntegerField(default=1)
#     x = models.IntegerField(default=0)
#     y = models.IntegerField(default=0)
#     created = models.DateTimeField('Creation Time', default=timezone.now)
#     def __str__(self):
#         return f'{self.id} | {self.name}'
#     @staticmethod
#     def get_model_from_seed_dict(dict):
#         return Region(name=dict["name"], min_level=dict["min_level"], max_level=dict["max_level"])

# class BiomeType(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     created = models.DateTimeField('Creation Time', default=timezone.now)

# class Biome(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.CharField(max_length=500)
#     biome_type = models.ForeignKey(BiomeType)
#     region = models.ForeignKey(Region, on_delete=models.CASCADE)
#     height = models.IntegerField(default=1)
#     width = models.IntegerField(default=1)
#     x = models.IntegerField(default=0)
#     y = models.IntegerField(default=0)
#     created = models.DateTimeField('Creation Time', default=timezone.now)

# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     biome = models.ForeignKey(Biome, on_delete=models.CASCADE)
#     location_type = models.ForeignKey(LocationType)
#     height = models.IntegerField(default=0)
#     width = models.IntegerField(default=0)
#     x = models.IntegerField(default=0)
#     y = models.IntegerField(default=0)
#     created = models.DateTimeField('Creation Time')

# class LocationType(models.Model):
#     name = models.CharField(max_length=100)
#     created = models.DateTimeField('Creation Time')