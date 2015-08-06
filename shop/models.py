from django.db import models
from django.forms import ModelForm
from django import forms
from django.dispatch import receiver
from django.contrib.auth.models import User
import os, json
from django.core import serializers
from os.path import join
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    widht = models.CharField(max_length=500, default="400px")
    heigth = models.CharField(max_length=500, default="300px")
    
class Category(models.Model):
    category_father = models.ForeignKey('self', null=True, blank=True, default = None)
    video = models.ForeignKey(Video, null=True, blank=True, default = None)
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='images/categories/<category_id>/', blank=True, null=True)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [('active', 'active'), ('inactive', 'inactive')]
    OPTIONS_PUB = [('published', 'published'), ('no published', 'no published')]
    SIZE_OPTIONS = [('XS','XS'),('S','S'),('M','M'),('L','L'),('XL','XL'),('XXL','XXL')]
    featured = models.BooleanField(default=True)
    published = models.CharField(max_length=50, choices = OPTIONS_PUB, default='published')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length = 10) 
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category)
    img = models.ImageField(upload_to='images/products/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    def getSizes(self):
        array = []
        sizes = self.size.split(";")
        for size in sizes:
            array.append(size)
        return array
    
    def getColors(self):
        array =[]
        colors = self.color.split(";")
        for color in colors:
            array.append(color)
        return array

class Stock(models.Model):
    quantity = models.IntegerField(max_length=5)
    product = models.ForeignKey(Product)
    def __unicode__(self):
        return self.product.name 
    
class SlideShow(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, default = None)
    product = models.ForeignKey(Product, null=True, blank=True, default = None)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    img = models.ImageField(upload_to='images/slider/', blank=True, null=True)
    
class Cart(models.Model):
    data = {}
    
class Customers(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    tagline = models.CharField(max_length=140, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    sournames = models.CharField(max_length=200)
    birthdate = models.DateField()
    email = models.EmailField()
    telephone = models.IntegerField(max_length=9)
    cart = Cart()
    
    def __unicode__(self):
        return self.user.username
    
    def calculatePrice(self):
        
        products = Product.objects.all()
        pro = []
        p={}
        x={}
        list=[]
        print "veixam"
        print self.cart.data
        for product in products:
            if(str(product.pk) in self.cart.data.keys()):
                pro.append(product.pk)
                print "coincidencia"
                p['pk']=product.pk
                x["total"]=self.cart.data[str(product.pk)]
                x["price"] =float(self.cart.data[str(product.pk)]*product.price)
                p['fields']=x
                list.append(p)
                p={}
        products = Product.objects.filter(pk__in=pro)
        print json.dumps(list)
        return {"products":products, "list":json.dumps(list)}

class Sales(models.Model):
    customer = models.ForeignKey(Customers, null=False, default=None)
    data = {}
    
class History_Status(models.Model):
    sale = models.ForeignKey(Sales, unique=False)
    msg = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
     
"""ARA ELS FORMULARIS PER EL FRONTEND"""

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')
        username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'fieldForm'}))

class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['name','sournames','birthdate','email','telephone']

