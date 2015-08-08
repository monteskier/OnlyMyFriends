# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20150807_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
