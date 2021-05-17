from django.contrib import admin

from .models import TreasureHoardTier, TreasureHoard, TreasureHoardRollTable
from .art_object_models import ArtObject, ArtObjectGroup, TreasureHoardArtObjectRoll, ArtObjectGroupEntry, ArtObjectTreasureHoardEntry
from .gem_models import Gem, GemGroup, TreasureHoardGemRoll, GemGroupEntry, GemTreasureHoardEntry
from .coin_models import Coin, CoinTreasureHoardEntry, TreasureHoardCoinRoll
from .magic_item_models import ItemSignifigance, MagicItem, MagicItemGroup, MagicItemGroupEntry, MagicItemInstance, MagicItemTreasureHoardEntry, MagicItemType, TreasureHoardMagicItemRoll

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
