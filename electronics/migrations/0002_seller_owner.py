# Generated by Django 5.0.4 on 2024-05-07 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
            preserve_default=False,
        ),
    ]
