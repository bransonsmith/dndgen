from rest_framework import serializers
from ..models.location_models import *

class RollTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RollTable
        fields = ('id', 'name', 'description', 'created')