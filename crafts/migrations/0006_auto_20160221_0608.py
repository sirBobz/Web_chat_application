# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0005_auto_20160210_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftpost',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
