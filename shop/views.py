from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category
from django.http import Http404
# Create your views here.

def index(request):
    try:
        products = Product.objects.all().filter(featured=True, published='published')
        category = Category.objects.all()
    except:
        raise Http404('Cap producte Disponible')

    return render(request, 'products/index.html',{'products':products,'categories':category})

def detailProduct(request, product_id):
    return HttpResponse("Esta intentat veure les propietats del objecte %s" % product_id)

def productsOfCategory(request, category_id):
    try:
        products = Product.objects.all().filter(published='published', category=category_id)
        categorySelect = Category.objects.get(pk=category_id)
        categoryAll = Category.objects.all()
    except:
        raise Http404('Cap producte publicat dintre aquesta Categoria')
    
    return render(request,'products/productsOfCategory.html',{'products':products, 'categorySelect':categorySelect, 'categories':categoryAll})