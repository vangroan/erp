# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account_number',
            field=models.CharField(default='AAA', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 14, 1, 42, 359228, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 14, 1, 46, 997755, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
