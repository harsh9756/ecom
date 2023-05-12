from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register((mainCategory,
                     subCategory,
                     Brand,
                     Product,
                     Seller))
