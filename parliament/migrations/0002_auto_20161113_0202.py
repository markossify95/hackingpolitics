# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speech',
            name='member',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='profession',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='city',
        ),
        migrations.AddField(
            model_name='member',
            name='bio',
            field=models.TextField(default='', max_length=36000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='board_type',
            field=models.IntegerField(default=-1),
        ),
        migrations.DeleteModel(
            name='Speech',
        ),
    ]