from django.contrib import admin

from .models.models import *
from .models.art_object_models import *
from .models.gem_models import *
from .models.coin_models import *
from .models.magic_item_models import *
from .models.monster_models import *

admin.site.register(TreasureHoardTier)
admin.site.register(TreasureHoard)
admin.site.register(TreasureHoardRollTable)

admin.site.register(ArtObject)
admin.site.register(ArtObjectGroup)
admin.site.register(TreasureHoardArtObjectRoll)
admin.site.register(ArtObjectGroupEntry)
admin.site.register(ArtObjectTreasureHoardEntry)

admin.site.register(Gem)
admin.site.register(GemGroup)
admin.site.register(TreasureHoardGemRoll)
admin.site.register(GemGroupEntry)
admin.site.register(GemTreasureHoardEntry)

admin.site.register(Coin)
admin.site.register(CoinTreasureHoardEntry)
admin.site.register(TreasureHoardCoinRoll)

admin.site.register(ItemSignifigance) 
admin.site.register(MagicItem) 
admin.site.register(MagicItemGroup) 
admin.site.register(MagicItemGroupEntry) 
admin.site.register(MagicItemInstance) 
admin.site.register(MagicItemTreasureHoardEntry) 
admin.site.register(MagicItemType) 
admin.site.register(TreasureHoardMagicItemRoll)

admin.site.register(CreatureSize)
admin.site.register(MonsterType)
admin.site.register(MonsterSubType)
admin.site.register(Race)
admin.site.register(Monster)
