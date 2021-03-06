# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 22:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_auto_20170614_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('ordering', models.IntegerField()),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('ordering', models.PositiveSmallIntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=2)),
                ('tag', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='checklist.Checklist')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.DeleteModel(
            name='ListItem',
        ),
    ]
