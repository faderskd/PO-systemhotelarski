# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_reservation_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
