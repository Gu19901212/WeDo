# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-15 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_auto_20190614_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
