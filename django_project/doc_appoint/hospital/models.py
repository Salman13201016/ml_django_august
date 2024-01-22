from django.db import models
from division.models import Divisions
from district.models import Districts
from station.models import Stations
from hospital_category.models import Hospital_Category

# Create your models here.

class Hospitals(models.Model):
    name = models.CharField(max_length=200)
    div_id = models.ForeignKey(Divisions, models.CASCADE)
    dis_id = models.ForeignKey(Districts, models.CASCADE)
    station_id = models.ForeignKey(Stations, models.CASCADE)
    cat_id = models.ForeignKey(Hospital_Category, models.CASCADE)
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    web_link = models.CharField(max_length=500)
    description = models.TextField()