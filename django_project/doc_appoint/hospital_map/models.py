from django.db import models
from hospital.models import Hospitals

# Create your models here.

class Hospital_Maps(models.Model):
    lat = models.CharField(max_length=200, default=None)
    long = models.CharField(max_length=200)
    hos_id = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    