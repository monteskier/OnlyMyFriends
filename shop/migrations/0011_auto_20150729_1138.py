# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=None, to='shop.Customers'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(default=None, to='shop.Customers'),
        ),
    ]
