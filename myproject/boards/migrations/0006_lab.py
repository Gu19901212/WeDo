# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-05 18:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0005_auto_20190606_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('teachers', models.CharField(max_length=50)),
                ('direction', models.CharField(max_length=50)),
                ('staff', models.IntegerField()),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='boards.Board')),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]