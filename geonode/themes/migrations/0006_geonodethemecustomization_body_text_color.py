# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_themes', '0005_auto_20190510_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='body_text_color',
            field=models.CharField(default=b'#3a3a3a', max_length=10),
        ),
    ]