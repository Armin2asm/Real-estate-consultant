from django.contrib import admin
from .models import Property,PropertyImage
# Register your models here.
@admin.register(Property)

class PropertyAdmin(admin.ModelAdmin):
    list_display=('owner','title','transaction_type','property_type','owner_name','city','owner_phone','address','area','bedrooms','floor','year_built','parking','elevator','storage_room','sale_price','rent_price','description','is_active','created_at')
    
@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display=('image','property')
