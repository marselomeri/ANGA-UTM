# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-04 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notams', '0002_auto_20180301_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='notamairspace',
            name='notam_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='notamairspace',
            name='reason',
            field=models.CharField(blank=True, help_text=' Reason for NOTAM', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='notamairspace',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'PENDING'), (1, 'ACTIVE')], default=0, null=True),
        ),
    ]
