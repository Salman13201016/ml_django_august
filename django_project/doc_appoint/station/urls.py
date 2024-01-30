from django.contrib import admin
from django.urls import path

from . import views as v

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path("", v.index, name="station_index"),
    path("insert/", v.insert, name="station_insert"),
    path("get_districts/", v.get_districts, name="get_districts"),
]
=======
    path("", v.index, name='station_index'),
    path("insert/", v.insert, name='station_insert'),
    path("get_districts/", v.get_districts, name='get_districts'),
]
>>>>>>> hospital_module
=======
    path("", v.index, name='station_index'),
    path("insert/", v.insert, name='station_insert'),
    path("get_districts/", v.get_districts, name='get_districts'),
]
>>>>>>> hospital_map_module
