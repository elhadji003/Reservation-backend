
from rest_framework import serializers
from ..models import Slot
from rest_framework.fields import DateTimeField

class SlotSerializer(serializers.ModelSerializer):
    start_time = DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    end_time = DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    image1 = serializers.ImageField(use_url=True, required=False, allow_null=True)
    image2 = serializers.ImageField(use_url=True, required=False, allow_null=True)
    image3 = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Slot
        fields = [
            "id", "title", "is_booked", "category", "rating",
            "start_time", "end_time", "map", "image1", "image2", "image3", "resource"
        ]
