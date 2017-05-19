# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='craftpost',
            name='postcategory',
            field=models.CharField(default='Craft', max_length=2, choices=[('Craft', 'Craft'), ('Food', 'Food')]),
        ),
    ]
