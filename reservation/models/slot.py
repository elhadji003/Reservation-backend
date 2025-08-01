from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .resource import Resource
from .facility import Facility
from django.conf import settings  # pour settings.AUTH_USER_MODEL

class Slot(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="slots"
    )
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="slots")
    facilities = models.ManyToManyField(Facility, blank=True, related_name="slots")
    title = models.CharField(max_length=100)
    is_booked = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    map = models.CharField(max_length=100)

    image1 = CloudinaryField('image', blank=True, null=True)
    image2 = CloudinaryField('image', blank=True, null=True)
    image3 = CloudinaryField('image', blank=True, null=True)

    class Meta:
        unique_together = ("resource", "start_time", "end_time")
        ordering = ["start_time"]

    def __str__(self):
        return f"{self.resource.name} - {self.start_time} à {self.end_time}"
