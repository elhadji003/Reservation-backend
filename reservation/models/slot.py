from django.db import models
from .resource import Resource

class Slot(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="slots")
    title = models.CharField(max_length=100)
    is_booked = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    map = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='slots/', blank=True, null=True)
    image2 = models.ImageField(upload_to='slots/', blank=True, null=True)
    image3 = models.ImageField(upload_to='slots/', blank=True, null=True)

    class Meta:
        unique_together = ("resource", "start_time", "end_time")
        ordering = ["start_time"]

    def __str__(self):
        return f"{self.resource.name} - {self.start_time} à {self.end_time}"
