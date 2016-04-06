# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0003_auto_20160406_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorderline',
            name='stockitem',
            field=models.ForeignKey(to='distribution.StockItem', default=1),
            preserve_default=False,
        ),
    ]
