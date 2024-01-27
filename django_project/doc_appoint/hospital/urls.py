from django.urls import path

from . import views 

urlpatterns = [
    path("", views.hospital_index,name='hospital_index'),
    path("hospital_insert/", views.hospital_insert,name='hospital_insert'),
    path('get_districts/', views.get_districts, name='get_districts'),
    path('get_stations/', views.get_stations, name='get_stations'),
]