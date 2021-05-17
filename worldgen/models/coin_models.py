from .models import TreasureHoard, TreasureHoardRollTable, TreasureHoardTier
from django.db import models
from django.utils import timezone

class Coin(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=10)
    value = models.DecimalField(default=1.0, max_digits=20, decimal_places=10)
    description = models.CharField(max_length=200, default='')
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return Coin(name=dict["name"], value=dict["value"], abbreviation=dict["abbreviation"], description=dict["description"])

# Ex: a roll on a hoard table would give 2d4 objects from group X
class TreasureHoardCoinRoll(models.Model):
    treasure_hoard_roll = models.ForeignKey(TreasureHoardRollTable, on_delete=models.CASCADE)
    dice = models.CharField(max_length=100)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.treasure_hoard_roll.min_roll}-{self.treasure_hoard_roll.max_roll}) {self.dice} {self.coin.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        dice = dict["coin_dice"]
        tier = TreasureHoardTier.objects.all().filter(name=dict["tier"]).first()
        treasure_hoard_roll = TreasureHoardRollTable.objects.all().filter(tier=tier, min_roll=dict["min_roll"], max_roll=dict["max_roll"]).first()            
        coin = Coin.objects.filter(abbreviation=dict["coin_brev"]).first()
        return TreasureHoardCoinRoll(treasure_hoard_roll=treasure_hoard_roll, dice=dice, coin=coin)

class CoinTreasureHoardEntry(models.Model):
    treasure_hoard = models.ForeignKey(TreasureHoard, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.quantity} {self.coin.abbreviation} in {self.treasure_hoard.name}'
