# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20170326_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdata',
            name='tooltip',
            field=models.CharField(max_length=1000),
        ),
    ]
