from rest_framework import serializers
from ..models import Slot, Facility
from .facility import FacilitySerializer

class SlotSerializer(serializers.ModelSerializer):
    facilities = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Facility.objects.all()
    )
    facilities_details = FacilitySerializer(source="facilities", many=True, read_only=True)

    image1 = serializers.ImageField(required=False, allow_null=True)
    image2 = serializers.ImageField(required=False, allow_null=True)
    image3 = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Slot
        fields = [
            "id", "title", "is_booked", "category", "rating",
            "start_time", "end_time", "map",
            "image1", "image2", "image3",
            "facilities", "facilities_details", "resource"
        ]
        read_only_fields = ["user"]