from django.db import models

# Create your models here.
class AgentsName(models.Model):
    statuschoice=(('Man','Man'),('Woman','Woman'))
    name=models.CharField(max_length= 50)
    last_name=models.CharField(max_length= 50)
    age=models.IntegerField()
    gender=models.CharField(choices=statuschoice)
    profile=models.ImageField(upload_to='Agent/')
    