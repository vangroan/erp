# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20160405_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('description', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('prefix', models.CharField(max_length=20)),
                ('reference', models.CharField(max_length=50)),
                ('status', models.CharField(default='E', choices=[('E', 'Entered'), ('U', 'Unprocessed'), ('P', 'Processed'), ('C', 'Cancelled')], max_length=1)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('customer_account_number', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesOrderLine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('sales_order', models.ForeignKey(to='distribution.SalesOrder')),
            ],
        ),
    ]
