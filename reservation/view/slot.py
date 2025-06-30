from rest_framework import viewsets, permissions
from reservation.models import Slot
from reservation.serializers.slot import SlotSerializer

class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Tu peux ajouter filtres, permissions spécifiques ici
