# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20170404_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdata',
            name='guildWarehouseStorable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='itemdata',
            name='storeSellable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='itemdata',
            name='tradeable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='itemdata',
            name='warehouseStorable',
            field=models.BooleanField(default=True),
        ),
    ]
