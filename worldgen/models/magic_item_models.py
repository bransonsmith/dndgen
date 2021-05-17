from .models import TreasureHoard, TreasureHoardRollTable, Rarity, ContentSource, TreasureHoardTier
from django.db import models
from django.utils import timezone

class MagicItemGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=150, default='')
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return MagicItemGroup(name=dict["name"], description=dict["description"])

# Ex: a roll on a hoard table would give 2d4 objects from group X
class TreasureHoardMagicItemRoll(models.Model):
    treasure_hoard_roll = models.ForeignKey(TreasureHoardRollTable, on_delete=models.CASCADE)
    dice = models.CharField(max_length=100)
    magic_item_group = models.ForeignKey(MagicItemGroup, on_delete=models.CASCADE)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.treasure_hoard_roll.min_roll}-{self.treasure_hoard_roll.max_roll}) {self.dice} {self.magic_item_group.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        dice = dict["magic_dice"]
        tier = TreasureHoardTier.objects.all().filter(name=dict["tier"]).first()
        treasure_hoard_roll = TreasureHoardRollTable.objects.all().filter(tier=tier, min_roll=dict["min_roll"], max_roll=dict["max_roll"]).first()            
        magic_item_group = MagicItemGroup.objects.filter(name=dict["magic_group"]).first()
        return TreasureHoardMagicItemRoll(treasure_hoard_roll=treasure_hoard_roll, dice=dice, magic_item_group=magic_item_group)  
        
class MagicItemType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return MagicItemType(name=dict["name"])
        
class ItemSignifigance(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        return ItemSignifigance(name=dict["name"])
        
class MagicItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    magic_item_type = models.ForeignKey(MagicItemType, on_delete=models.CASCADE)
    signifigance = models.ForeignKey(ItemSignifigance, on_delete=models.CASCADE)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    attunement = models.BooleanField(default=False)
    source = models.ForeignKey(ContentSource, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='')
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
        
class MagicItemInstance(models.Model):
    name = models.CharField(max_length=100)
    magic_item = models.ForeignKey(MagicItem, on_delete=models.CASCADE)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.name}'
        
class MagicItemGroupEntry(models.Model):
    magic_item = models.ForeignKey(MagicItem, on_delete=models.CASCADE)
    magic_item_group = models.ForeignKey(MagicItemGroup, on_delete=models.CASCADE)
    extra_dice = models.CharField(max_length=100, default="")
    extra_group = models.ForeignKey(MagicItemGroup, on_delete=models.CASCADE, default=None, related_name='extra_group', blank=True, null=True)
    min_roll = models.IntegerField()
    max_roll = models.IntegerField()
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | ({self.min_roll}-{self.max_roll}) {self.magic_item.name} > {self.magic_item_group.name}'
    @staticmethod
    def get_model_from_seed_dict(dict):
        magic_item_group = MagicItemGroup.objects.all().filter(name__iexact=dict["group_name"]).first()
        magic_item = MagicItem.objects.all().filter(name__iexact=dict["item_name"]).first()
        extra_dice = ""
        extra_group = None
        if "extra_dice" in dict.keys():
            extra_dice = dict["extra_dice"]
            extra_group = MagicItemGroup.objects.all().filter(name__iexact=dict["roll_in"]).first()
        return MagicItemGroupEntry(magic_item=magic_item, magic_item_group=magic_item_group, min_roll=dict["min_roll"], max_roll=dict["max_roll"], extra_dice=extra_dice, extra_group=extra_group)
     
class MagicItemTreasureHoardEntry(models.Model):
    treasure_hoard = models.ForeignKey(TreasureHoard, on_delete=models.CASCADE)
    magic_item_instance = models.ForeignKey(MagicItemInstance, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField('Creation Time', default=timezone.now)
    def __str__(self):
        return f'{self.id} | {self.quantity} {self.magic_item.name} in {self.treasure_hoard.name}'
