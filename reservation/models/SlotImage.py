from django.db import models

class SlotImage(models.Model):
    slot = models.ForeignKey("Slot", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="slot_images/")
    