from django.contrib import admin
from django.urls import path

from . import views as v

urlpatterns = [
    path("", v.index, name='station_index'),
    path("insert/", v.insert, name='station_insert'),
    path("get_districts/", v.get_districts, name='get_districts'),
]