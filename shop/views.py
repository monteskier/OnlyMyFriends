from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Stock, Cart
from .models import Category
from .models import SlideShow
from .models import CustomerForm, UserForm
from django.core import serializers
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
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

def register(request):
    registered = False
    if request.method == 'POST':
        customer_form = CustomerForm(data=request.POST)
        user_form = UserForm(data=request.POST)
        if customer_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            customer = customer_form.save(commit = False)
            customer.user = user
            customer.save()
            
            registered = True
        else:
            print customer_form.errors
    else:
        customer_form = CustomerForm()
        user_form = UserForm()
    return render(request,'customers/register.html',{'user_form':user_form,'customer_form':customer_form, 'registered':registered})

def customerLogin(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your acount is dissabled")
        else:
            print "Invalid login details; {0},{1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,"customers/login.html",{})

def customerLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def detailProduct(request, product_id):
    product = Product.objects.get(pk=product_id)
    categoryAll = Category.objects.all()
    categorySelect = Category.objects.get(pk=product.category.pk)
    stock = Stock.objects.get(product=product.pk)
    
    return render(request,'products/detailProduct.html',{'categories':categoryAll, 'product':product,'categorySelect':categorySelect,'stock':stock})

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

"""SHOPINGCART"""
def addToShopingCart(request, total, product_id):
    if request.method=="POST":
        try:
            pass
        except:
            pass
        
    pass        
        
