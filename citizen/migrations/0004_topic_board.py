# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0005_auto_20161113_1313'),
        ('citizen', '0003_auto_20161113_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parliament.Board'),
            preserve_default=False,
        ),
    ]