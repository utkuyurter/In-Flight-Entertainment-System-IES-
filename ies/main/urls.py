from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('restroom/', views.restroom, name='restroom'),
]


