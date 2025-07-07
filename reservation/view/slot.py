from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reservation.models import Slot, Facility
from reservation.serializers.slot import SlotSerializer, FacilitySerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        # Si l'utilisateur est admin, il voit uniquement ses slots
        if user.is_authenticated and user.is_staff:
            return Slot.objects.filter(user=user)

        # Si c'est un utilisateur non authentifié ou simple client, il voit tous les slots
        return Slot.objects.all()



class FacilityViewSet(ReadOnlyModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer