# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0003_auto_20170416_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='items',
        ),
    ]
