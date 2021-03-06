# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-31 12:10
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirportGeofences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('centroid', django.contrib.gis.db.models.fields.PointField(default='POINT(37.943 23.715)', srid=4326)),
            ],
        ),
    ]
