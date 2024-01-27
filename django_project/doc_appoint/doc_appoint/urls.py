"""
URL configuration for doc_appoint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from . import views as v

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("admin/role/", include('role.urls')),
    path("admin/user/", include('user.urls')),
    path("admin/division/", include('division.urls')),
    path("admin/district/", include('district.urls')),
    path("admin/hospital_category/", include('hospital_category.urls')),
    path("admin/station/", include('station.urls')),
    path("admin/hospital/", include('hospital.urls')),
    path("login/", include('auth_user.urls')),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path("admin/hospital_map/", include('hospital_map.urls')),
]
