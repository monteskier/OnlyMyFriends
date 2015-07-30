# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20150730_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='cart',
            field=models.OneToOneField(to='shop.Cart'),
        ),
    ]
