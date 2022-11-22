from django.urls import path
from . import views


urlpatterns = [
    path('', views.Testemonials.as_view(), name='testemonials'),
]
