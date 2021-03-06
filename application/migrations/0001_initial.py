# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('plot', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('imdbid', models.CharField(blank=True, max_length=9, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
