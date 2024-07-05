from django.db import models
from django.contrib.auth.models import User
import datetime 
import os 

def getFileName(request,filename): 
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    fileName =  "%s%s"%(nowTime,filename)
    return os.path.join('uploads/',fileName)
class Category(models.Model): 
    NAME = models.CharField(max_length=100,blank=False,null=False)
    IMAGE = models.ImageField(upload_to= getFileName,null=True,blank=True)
    DESCRIPTION = models.TextField(max_length=500,null=False,blank=False)
    STATUS = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    CREATE = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.NAME

class Product(models.Model): 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    NAME = models.CharField(max_length=100,blank=False,null=False)
    VENDOR = models.CharField(max_length=100,blank=False,null=False)
    PRODUCT_IMAGE = models.ImageField(upload_to= getFileName,null=True,blank=True)
    QUANTITY = models.IntegerField(null=False,blank=False)
    ORIGINAL_PRICE = models.FloatField(null=False,blank=False)
    SELLING_PRICE = models.FloatField(null=False,blank=False)
    DESCRIPTION = models.TextField(max_length=500,null=False,blank=False)
    STATUS = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    TRENDING = models.BooleanField(default=False,help_text="0-default,1-Trending")
    CREATE = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.NAME

class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product, on_delete=models.CASCADE)
    PRODUCT_QTY = models.IntegerField(null=False, blank=False)
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self): 
        return self.PRODUCT_QTY * self. PRODUCT.SELLING_PRICE
    

class Favourite(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product, on_delete=models.CASCADE)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    