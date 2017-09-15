# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='blogs',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]