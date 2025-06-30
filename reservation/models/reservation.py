from django.db import models
from django.conf import settings
from .slot import Slot

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reservations")
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    calendar_link = models.URLField(blank=True, null=True)  # ✅ ce champ doit exister
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "En attente"),
            ("confirmed", "Confirmée"),
            ("cancelled", "Annulée"),
        ],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.slot}"
