# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20150730_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='cart',
        ),
    ]
