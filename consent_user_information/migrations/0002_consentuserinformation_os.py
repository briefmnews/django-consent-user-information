# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent_user_information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consentuserinformation',
            name='os',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]