# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('category', models.ForeignKey(to='shop.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('widht', models.CharField(default=b'400px', max_length=500)),
                ('heigth', models.CharField(default=b'300px', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='S', max_length=10, choices=[(b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='product',
            field=models.ForeignKey(to='shop.Product', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='video',
            field=models.ForeignKey(to='shop.Video', null=True),
        ),
    ]
