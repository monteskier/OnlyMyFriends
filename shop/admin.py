from django.contrib import admin
from django.utils import timezone
from models import Product, Category, Stock, Customers, Sales, History_Status

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


# Register your models here.
