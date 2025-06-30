
from rest_framework import serializers
from ..models import Slot
from rest_framework.fields import DateTimeField

class SlotSerializer(serializers.ModelSerializer):
    start_time = DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    end_time = DateTimeField(format="%Y-%m-%d %H:%M", required=False)
    image1 = serializers.SerializerMethodField()
    image2 = serializers.SerializerMethodField()
    image3 = serializers.SerializerMethodField()

    class Meta:
        model = Slot
        fields = [
            "id", "title", "is_booked", "category", "rating",
            "start_time", "end_time", "map", "image1", "image2", "image3", "resource"
        ]

    def get_image1(self, obj):
        return obj.image1.url if obj.image1 else None

    def get_image2(self, obj):
        return obj.image2.url if obj.image2 else None

    def get_image3(self, obj):
        return obj.image3.url if obj.image3 else None
