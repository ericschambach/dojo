# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookslikes_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='notes',
        ),
    ]
