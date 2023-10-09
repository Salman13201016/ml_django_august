from django.db import models

class demo_user(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length = 500)
    image = models.ImageField(upload_to='images/')
