# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150722_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='img',
            field=models.ImageField(null=True, upload_to=b'images/slider/', blank=True),
        ),
    ]
