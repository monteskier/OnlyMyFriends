# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_slideshow_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='category',
            field=models.ForeignKey(default=None, blank=True, to='shop.Category', null=True),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='product',
            field=models.ForeignKey(default=None, blank=True, to='shop.Product', null=True),
        ),
    ]
