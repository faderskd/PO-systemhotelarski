# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 14:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 1, 7, 14, 52, 17, 648495, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
