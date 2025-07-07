from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reservation.models import Reservation
from rest_framework.permissions import IsAuthenticated
from reservation.serializers.serializers import ReservationCreateSerializer, ReservationDetailSerializer
from reservation.utils.email import send_reservation_confirmation_email


class ReservationAllView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_staff:
            # Admin : voit les réservations liées à SES slots
            reservations = Reservation.objects.filter(slot__user=user).select_related("slot", "user")
        else:
            # Client : voit ses propres réservations
            reservations = Reservation.objects.filter(user=user).select_related("slot", "user")

        serializer = ReservationDetailSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReservationCreateSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()

            # Récupérer le slot lié à la réservation
            slot = reservation.slot  # Adapter selon ton modèle

            # Envoi email de confirmation
            try:
                send_reservation_confirmation_email(
                    reservation.user,
                    slot,
                    reservation.calendar_link
                )
            except Exception as e:
                print("Erreur envoi email :", e)

            return Response({
                "message": "Réservation créée avec succès",
                "reservation_id": reservation.id,
                "calendar_link": reservation.calendar_link
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReservationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk, user=request.user)
        except Reservation.DoesNotExist:
            return Response({"error": "Réservation introuvable"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReservationDetailSerializer(reservation)
        return Response(serializer.data)

class MyReservationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservations = Reservation.objects.filter(user=request.user).select_related("slot")
        serializer = ReservationDetailSerializer(reservations, many=True)
        return Response(serializer.data)

# --- Nouveaux endpoints ---

class ReservationCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk, user=request.user)
        except Reservation.DoesNotExist:
            return Response({"error": "Réservation introuvable"}, status=status.HTTP_404_NOT_FOUND)

        slot = reservation.slot
        slot.is_booked = False
        slot.save()

        # Annule la réservation
        reservation.status = "cancelled"
        reservation.save()

        return Response({"message": "Réservation annulée"}, status=status.HTTP_200_OK)

class ReservationDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk, user=request.user)
        except Reservation.DoesNotExist:
            return Response({"error": "Réservation introuvable"}, status=status.HTTP_404_NOT_FOUND)
        # Libérer le slot
        slot = reservation.slot
        slot.is_booked = False
        slot.save()
        # Supprimer la réservation
        reservation.delete()
        return Response({"message": "Réservation supprimée"}, status=status.HTTP_204_NO_CONTENT)
