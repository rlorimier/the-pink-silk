from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_packages, name='packages'),
    path('<package_id>', views.package_detail, name='package_detail'),
]
