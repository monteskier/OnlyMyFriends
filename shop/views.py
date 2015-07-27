from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category
from .models import SlideShow
from django.core import serializers
from django.http import Http404
import json
# Create your views here.

def index(request):
    try:
        products = Product.objects.all().filter(featured=True, published='published')
        category = Category.objects.all().filter(category_father=None)
        sliders  = SlideShow.objects.all()
    except:
        raise Http404('Cap producte Disponible')
    
    
    return render(request, 'products/index.html',{'products':products,'categories':category, 'sliders':sliders})

def detailProduct(request, product_id):
    product = Product.objects.get(pk=product_id)
    categoryAll = Category.objects.all()
    categorySelect = Category.objects.get(pk=product.category.pk)
    
    return render(request,'products/detailProduct.html',{'categories':categoryAll, 'product':product,'categorySelect':categorySelect})

def categoryChilds(request, category_id):
    try:
        category = serializers.serialize('json', Category.objects.all().filter(category_father=category_id));
        print category;
        return HttpResponse(category);
    except:
        return HttpResponse("sense fills");
        
def productsOfCategory(request, category_id):
    try:
        products = Product.objects.all().filter(published='published', category=category_id)
        categorySelect = Category.objects.get(pk=category_id)
        category = Category.objects.all().filter(category_father=None)
    except:
        raise Http404('Cap producte publicat dintre aquesta Categoria')
    
    return render(request,'products/productsOfCategory.html',{'products':products, 'categorySelect':categorySelect, 'categories':category})