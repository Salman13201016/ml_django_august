from django.urls import path

<<<<<<< HEAD
from . import views

urlpatterns = [
    path("", views.hospital_index, name="hospital_index"),
    path("hospital_insert/", views.hospital_insert, name="hospital_insert"),
    path("get_districts/", views.get_districts, name="get_districts"),
    path("get_stations/", views.get_stations, name="get_stations"),
]
=======
from django.conf import settings
from django.conf.urls.static import static

from . import views 

urlpatterns = [
    path("", views.hospital_index,name='hospital_index'),
    path("hospital_insert/", views.hospital_insert,name='hospital_insert'),
    path('get_districts/', views.get_districts, name='get_districts'),
    path('get_stations/', views.get_stations, name='get_stations'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
>>>>>>> hospital_module
