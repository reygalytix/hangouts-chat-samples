# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productivity_bot', '0003_auto_20180615_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeloops',
            name='webhook_id',
        ),
    ]
