# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0004_auto_20160208_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftpost',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads', null=True),
        ),
    ]
