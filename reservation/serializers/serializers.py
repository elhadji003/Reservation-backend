from rest_framework import serializers
from reservation.models import Reservation, Slot
from django.contrib.auth import get_user_model

User = get_user_model()

from reservation.utils.google_calendar import add_event_to_google_calendar

class ReservationCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    slot_id = serializers.IntegerField()

    def validate(self, data):
        try:
            slot = Slot.objects.get(pk=data['slot_id'])
        except Slot.DoesNotExist:
            raise serializers.ValidationError("Le créneau n'existe pas.")
        if slot.is_booked:
            raise serializers.ValidationError("Le créneau est déjà réservé.")

        data['slot'] = slot
        return data

    def create(self, validated_data):
        email = validated_data['email']
        slot = validated_data['slot']

        user, _ = User.objects.get_or_create(email=email, defaults={'username': email.split('@')[0]})

        # ✅ Ajouter à Google Calendar
        try:
            calendar_link = add_event_to_google_calendar(slot)
        except Exception as e:
            print("Erreur lors de l'ajout au calendrier :", e)
            calendar_link = None

        # ✅ Créer la réservation avec le lien
        reservation = Reservation.objects.create(
            user=user,
            slot=slot,
            status="confirmed",
            calendar_link=calendar_link
        )

        slot.is_booked = True
        slot.save()

        return reservation

class ReservationDetailSerializer(serializers.ModelSerializer):
    slot = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['id', 'slot', 'calendar_link', 'status']

    def get_slot(self, obj):
        return {
            "title": obj.slot.title,
            "start_time": obj.slot.start_time,
            "end_time": obj.slot.end_time,
        }
    
