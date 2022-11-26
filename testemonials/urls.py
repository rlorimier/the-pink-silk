from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_testemonials, name='testemonials'),
    path('new/', views.new_testemonial, name='new_testemonial'),
    path(
        'comment/<int:pk>/',
        views.comment_testemonial, name='comment_testemonial'),
]
