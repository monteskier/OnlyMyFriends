# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20150730_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='customers',
            name='cart',
            field=models.OneToOneField(default=None, to='shop.Cart'),
        ),
    ]
