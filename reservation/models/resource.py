from django.db import models

class Resource(models.Model):

    TYPES_CHOICE = [
        ('room', 'Chambre'),
        ('office', 'Bureau privé'),
        ('coworking', 'Espace de Travail'),
        ('meet', 'Salle de Reunion'),
        ('formation', 'Salle de Formation')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=100, choices=TYPES_CHOICE, default='room')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
