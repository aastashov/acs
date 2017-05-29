# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170523_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrate',
            name='id_finger',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='ID \u043f\u0430\u043b\u044c\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='administrate',
            name='address',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='administrate',
            name='gender',
            field=models.CharField(choices=[('\u041c', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), ('F', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')], max_length=2, null=True, verbose_name='\u041f\u043e\u043b'),
        ),
        migrations.AlterField(
            model_name='administrate',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]
