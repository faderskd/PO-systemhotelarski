# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('start_date',)},
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_pk',
            field=models.PositiveIntegerField(validators=django.core.validators.MinValueValidator(0), default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
