__author__ = 'joaquin'
from django.conf.urls import url, static, patterns
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/detailProduct/$', views.detailProduct, name='detailProduct'),
    url(r'^category/+(?P<category_id>[0-9])+/$', views.productsOfCategory, name="productsOfCategory")
]
