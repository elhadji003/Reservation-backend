# Generated by Django 5.2.3 on 2025-07-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_facility'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='slots', to='reservation.facility'),
        ),
    ]
