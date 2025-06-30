# reservation/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservation.view.slot import SlotViewSet
from reservation.view.resource import ResourceViewSet
from reservation.views import ReservationCreateView, ReservationDetailView, MyReservationsView, ReservationCancelView, ReservationDeleteView

router = DefaultRouter()
router.register(r'slots', SlotViewSet)
router.register(r'resources', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reservations/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path("reservations/me/", MyReservationsView.as_view(), name="my-reservations"),
      path('reservations/<int:pk>/cancel/', ReservationCancelView.as_view(), name='reservation-cancel'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation-delete'),

]
