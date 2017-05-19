# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0008_auto_20160329_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='anon', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='craftpost',
            name='text',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
