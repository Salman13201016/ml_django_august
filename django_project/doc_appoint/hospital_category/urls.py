from django.urls import path

from . import views
<<<<<<< HEAD
<<<<<<< HEAD

urlpatterns = [
    path("", views.hospital_cat_index, name="hospital_cat_index"),
    path("hospital_cat_insert/", views.hospital_cat_insert, name="hospital_cat_insert"),
]
=======
=======
>>>>>>> hospital_map_module
urlpatterns = [
    path('', views.hospital_cat_index, name='hospital_cat_index'),
    path('hospital_cat_insert/', views.hospital_cat_insert, name='hospital_cat_insert'),
    
<<<<<<< HEAD
]
>>>>>>> hospital_module
=======
]
>>>>>>> hospital_map_module
