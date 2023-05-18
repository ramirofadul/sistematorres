
from django.contrib import admin 
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve

from rest_framework import permissions

urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_gradient.urls')),
    path('juicios/',include('apps.juicios.api.routers')),
]
