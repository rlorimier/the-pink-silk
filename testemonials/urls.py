from django.urls import path
from . import views


urlpatterns = [
    path('', views.Testemonials.as_view(), name='testemonials'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
