# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-30 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeting',
            name='language',
            field=models.TextField(default='en'),
        ),
    ]
