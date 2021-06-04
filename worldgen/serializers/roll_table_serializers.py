from django.db.models import fields
from rest_framework import serializers
from ..models.location_models import *

class RollTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollTable
        fields = ('id', 'name', 'description', 'created')

class LocationRollTableEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRollTableEntry
        fields = ('id', 'roll_table', 'location_type', 'order', 'roll_quantity')

class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = ('id', 'name', 'description')