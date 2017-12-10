# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 20:40
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(default='', upload_to='')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Marker',
            },
        ),
    ]
