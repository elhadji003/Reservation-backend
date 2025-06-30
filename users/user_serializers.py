# serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'avatar']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

