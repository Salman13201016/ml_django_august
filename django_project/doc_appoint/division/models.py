from django.db import models

class Divisions(models.Model):
    name = models.CharField(max_length=500,unique=True)
    
    

# Create your models here.
