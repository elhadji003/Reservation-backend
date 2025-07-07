
from rest_framework import serializers
from ..models.facility import Facility

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name", "icon"]
