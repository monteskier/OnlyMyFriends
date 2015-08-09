__author__ = 'joaquin'
from django.conf.urls import url, static, patterns
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.customerLogin, name='customerLogin'),
    url(r'^logout/$', views.customerLogout, name='customerLogout'),
    url(r'^(?P<product_id>[0-9]+)/detailProduct/$', views.detailProduct, name='detailProduct'),
    url(r'^category/+(?P<category_id>[0-9])+/$', views.productsOfCategory, name="productsOfCategory"),
    url(r'^categoryChilds/+(?P<category_id>[0-9])+/$', views.categoryChilds, name="categoryChilds"),
    url(r'^addToShopingCart/(?P<total>[0-9])/(?P<product_id>[0-9])/(?P<color>\w+)/(?P<size>\w+)/$', views.addToShopingCart, name="addToShopingCart"),
    url(r'^refreshShopingCart/$', views.refreshShopingCart, name="refreshShopingCart"),
    url(r'^shopingList/$', views.shopingList, name="shopingList"),
    url(r'^shopingDelItem/(?P<cart_id>[0-9]{1,9999})+/$', views.shopingDelItem, name="shopingDelItem"),
    url(r'^delAllListShoping/+$', views.delAllListShoping, name="delAllListShoping"),
    url(r'^pdfView/+$', views.pdfView, name="pdfView"),


]
