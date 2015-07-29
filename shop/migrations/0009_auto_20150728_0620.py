# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20150724_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='username',
            new_name='name',
        ),
    ]
