from django.db import models
from division.models import Divisions
from district.models import Districts

class Stations(models.Model):
    name = models.CharField(max_length=200)
    div_id = models.ForeignKey(Divisions, on_delete=models.CASCADE)
    dis_id = models.ForeignKey(Districts, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'div_id', 'dis_id')

    def __str__(self):
        return self.name
