# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20161204_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='rPrivKey',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='rPubKey',
        ),
    ]
