# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0007_auto_20160329_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='sally', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
