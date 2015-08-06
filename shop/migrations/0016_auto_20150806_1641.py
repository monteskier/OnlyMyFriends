# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_remove_customers_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(null=True, upload_to=b'images/categories/<category_id>/', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=10),
        ),
    ]
