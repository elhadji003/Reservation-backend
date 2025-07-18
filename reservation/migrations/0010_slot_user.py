# Generated by Django 5.2.3 on 2025-07-06 19:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0009_alter_slot_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='slots', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
