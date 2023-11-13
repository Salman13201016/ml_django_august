from django.db import models
from role.models import Role

class User(models.Model):
    role_id = models.ForeignKey(Role, models.CASCADE)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.TextField()
    pw = models.CharField(max_length=500)

# Create your models here.
