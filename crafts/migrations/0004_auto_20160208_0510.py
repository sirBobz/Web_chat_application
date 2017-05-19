# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0003_craftpost_postcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftpost',
            name='postcategory',
            field=models.CharField(default='Craft', choices=[('Craft', 'Craft'), ('Food', 'Food')], max_length=5),
        ),
    ]
