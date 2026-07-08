from django.db import models
from django.contrib.auth.models import User
# this is for homepage
class HomePage(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='HomePage/')
    
