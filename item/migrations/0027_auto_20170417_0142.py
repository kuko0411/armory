# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0026_itemdata_passivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='awkened',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='masterworked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='maxItemLevel',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='minItemLevel',
            field=models.IntegerField(null=True),
        ),
    ]
