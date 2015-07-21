# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('img', models.ImageField(null=True, upload_to=b'/uploads/images/categories/<category_id>/', blank=True)),
                ('category_father', models.ForeignKey(default=None, blank=True, to='shop.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tagline', models.CharField(max_length=140, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=100)),
                ('sournames', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='History_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('featured', models.BooleanField(default=True)),
                ('published', models.CharField(default=b'published', max_length=50, choices=[(b'published', b'published'), (b'no published', b'no published')])),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('color', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50, choices=[(b'active', b'active'), (b'inactive', b'inactive')])),
                ('img', models.ImageField(null=True, upload_to=b'images/products/', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.ForeignKey(to='shop.Customers')),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(max_length=5)),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
        ),
        migrations.AddField(
            model_name='history_status',
            name='sale',
            field=models.ForeignKey(to='shop.Sales'),
        ),
    ]
