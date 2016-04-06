# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('H', 'OnHold'), ('D', 'Discontinued')], default='A', max_length=1),
            preserve_default=False,
        ),
    ]
