# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-12 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200812_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='user.Post'),
            preserve_default=False,
        ),
    ]
