from django.contrib import admin
from .models import HomePage

# Register your models here.
@admin.register(HomePage)

class HomePageAdmin(admin.ModelAdmin):
    list_display=('image','title',)