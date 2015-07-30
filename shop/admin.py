from django.contrib import admin
from django.utils import timezone
from models import Product, Category, Stock, Customers, Sales, History_Status, SlideShow, Video, Cart

class ProductAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(Customers)
admin.site.register(Sales)
admin.site.register(History_Status)
admin.site.register(SlideShow)
admin.site.register(Video)
admin.site.register(Cart)


# Register your models here.
