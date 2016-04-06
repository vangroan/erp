# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0002_item_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='StockItem',
        ),
    ]
