# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('title', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]
