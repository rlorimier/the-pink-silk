from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_packages, name='packages'),
    path('<int:package_id>', views.package_detail, name='package_detail'),
    path('edit/<int:package_id>/', views.edit_package, name='edit_package'),
    path(
        'delete/<int:package_id>/',
        views.delete_package, name='delete_package'),
    path('add/', views.add_package, name='add_package'),
]
