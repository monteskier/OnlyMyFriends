# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150721_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='video',
            field=models.ForeignKey(default=None, blank=True, to='shop.Video', null=True),
        ),
    ]
