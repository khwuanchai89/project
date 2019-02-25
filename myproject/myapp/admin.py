from django.contrib import admin
from myapp.models import Product 

class ProductAdmin(admin.ModelAdmin): 
 field = ('name','price','category','image') 
 list_display = ('name','price','category') 
 list_filter = ('category',)
 list_editable = ('price','category')

admin.site.register(Product,ProductAdmin)