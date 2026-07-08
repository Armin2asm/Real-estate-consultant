from django.contrib import admin
from .models import AgentsName
# Register your models here.
@admin.register(AgentsName)

class AgentsNameAdmin(admin.ModelAdmin):
    list_display=('name','last_name','age','gender','profile')