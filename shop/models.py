from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
import os
from os.path import join
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your models here.
class Category(models.Model):
    category_father = models.ForeignKey('self', null=True, blank=True, default = None)
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='/uploads/images/categories/<category_id>/', blank=True, null=True)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [('active', 'active'), ('inactive', 'inactive')]
    OPTIONS_PUB = [('published', 'published'), ('no published', 'no published')]
    featured = models.BooleanField(default=True)
    published = models.CharField(max_length=50, choices = OPTIONS_PUB, default='published')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category)
    img = models.ImageField(upload_to='images/products/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.name

class Stock(models.Model):
    quantity = models.IntegerField(max_length=5)
    product = models.ForeignKey(Product)

class Customers(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    tagline = models.CharField(max_length=140, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=100)
    sournames = models.CharField(max_length=200)
    birthdate = models.DateField()
    email = models.EmailField()
    telephone = models.IntegerField(max_length=9)
    
    def __unicode__(self):
        return self.user.username


    
class Sales(models.Model):
    customer = models.ForeignKey(Customers)
    product = models.ForeignKey(Product)
    
class History_Status(models.Model):
    sale = models.ForeignKey(Sales, unique=False)
    msg = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
     

