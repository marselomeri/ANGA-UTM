# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpas', '0002_auto_20180402_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpas',
            name='payload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rpas.Payload'),
        ),
        migrations.AlterField(
            model_name='rpas',
            name='rpas_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rpas.RpasModel'),
        ),
    ]