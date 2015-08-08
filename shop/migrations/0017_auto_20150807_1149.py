# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20150806_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=None, to='shop.Customers'),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(default=None, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=None, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=None),
        ),
    ]
