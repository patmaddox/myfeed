# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='fetched_at',
            field=models.DateTimeField(null=True),
        ),
    ]
