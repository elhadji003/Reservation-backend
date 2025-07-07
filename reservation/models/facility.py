# models/facility.py
from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=10, blank=True, help_text="Ex: 🪑, 🌐, ☕, 🔐")

    def __str__(self):
        return self.name
