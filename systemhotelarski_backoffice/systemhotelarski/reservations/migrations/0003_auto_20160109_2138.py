# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20160109_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user_pk',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
