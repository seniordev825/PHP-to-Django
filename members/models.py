from django.db import models
from django.conf import settings
import datetime
# Create your models here.
class register(models.Model):
     email=models.CharField(max_length=50)
     password=models.CharField(max_length=50)
class profile(models.Model):
    user=models.CharField(max_length=50,blank=True, null=True)
    password=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=254,blank=True, null=True)
class Usercompany(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField(blank=True, null=True)
    address=models.TextField()
    code=models.IntegerField(blank=True, null=True)
    vat=models.IntegerField(blank=True, null=True)
class Userpayment(models.Model):
    bankname=models.CharField(max_length=50,default="")
    bankaccount=models.CharField(max_length=50, default="")
    swift=models.CharField(max_length=50,blank=True, null=True)
    vat=models.IntegerField(blank=True, null=True)
class client(models.Model):
     companyname=models.CharField(max_length=50)
     companycode=models.CharField(max_length=50)
     vatcode=models.CharField(max_length=50)
     address=models.CharField(max_length=50)
     email=models.EmailField(max_length=254)
class Invoice(models.Model):
     accountnumber=models.IntegerField()
     date=models.DateField()
     paydate=models.DateField()
     companyname=models.CharField(max_length=50,blank=True, null=True)
     companycode=models.CharField(max_length=50,blank=True, null=True)
     vatcode=models.CharField(max_length=50,blank=True, null=True)
     address=models.CharField(max_length=50,blank=True, null=True)
     email=models.EmailField(max_length=254,blank=True, null=True)
     
class Product(models.Model):
     title=models.CharField(max_length=50)
     price=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
     vat=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
     quantity=models.IntegerField(blank=True, null=True)
     totalprice=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
     subtotal=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
     tax=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
     sumprice=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,default=0)
     sumtax=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,default=0)
     sumtotal=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,default=0)
class Number(models.Model):
     quan=models.IntegerField(blank=True, null=True)
class Product1(models.Model):
     title=models.CharField(max_length=50)
     price=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
     unit=models.CharField(max_length=50)
     