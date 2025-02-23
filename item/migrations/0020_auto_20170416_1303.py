# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0019_auto_20170414_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='crystal1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crystal1', to='item.ItemData'),
        ),
        migrations.AlterField(
            model_name='item',
            name='crystal2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crystal2', to='item.ItemData'),
        ),
        migrations.AlterField(
            model_name='item',
            name='crystal3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crystal3', to='item.ItemData'),
        ),
        migrations.AlterField(
            model_name='item',
            name='crystal4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crystal4', to='item.ItemData'),
        ),
    ]
