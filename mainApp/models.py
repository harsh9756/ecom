from django.db import models

# Create your models here.

class mainCategory(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

class subCategory(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name 

class Product(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    maincat=models.ForeignKey(mainCategory,on_delete=models.CASCADE)
    subcat=models.ForeignKey(subCategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    baseprice=models.IntegerField()
    discount=models.IntegerField(default=0)
    finalPrice=models.IntegerField()
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    desc=models.TextField()
    stock=models.BooleanField(default=True)
    time=models.DateField(auto_now=True)
    pic1=models.ImageField(upload_to='productimg/')
    pic2=models.ImageField(upload_to='productimg/')
    pic3=models.ImageField(upload_to='productimg/')



    def __str__(self):
        return str(self.id) + " " + self.name
class Seller(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    username=models.CharField(max_length=50, unique=True)
    phone=models.IntegerField()
    pin=models.IntegerField(blank=True,null=True)
    city=models.CharField(max_length=50, default="",null=True,blank=True)
    state=models.CharField(max_length=50, default="",null=True,blank=True)
    def __str__(self):
        return str(self.id) + " " + self.name
