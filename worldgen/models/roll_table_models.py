from django.db import models
from django.utils import timezone

class RollTable(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, default='')
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return RollTable(name=dict["name"], description=dict["description"])
