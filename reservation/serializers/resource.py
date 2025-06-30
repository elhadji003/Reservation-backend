from rest_framework import serializers
from reservation.models import Resource
from .slot import SlotSerializer

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'location']

class ResourceDetailSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, read_only=True, source='slot_set')

    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'location', 'slots']
