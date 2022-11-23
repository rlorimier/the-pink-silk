from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_testemonials, name='testemonials'),
    path('new/', views.new_testemonial, name='new_testemonial'),
]
