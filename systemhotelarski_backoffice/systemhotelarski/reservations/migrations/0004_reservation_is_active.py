# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20160109_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
