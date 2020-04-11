from django.urls import path
from . import views

urlpatterns = [
    path('', views.multasestacionamiento_list, name='multasestacionamiento_list'),
    path('multasestacionamiento/<int:pk>/', views.multasestacionamiento_detail, name='multasestacionamiento_detail'),
    path('multasestacionamiento/new', views.multasestacionamiento_new, name='multasestacionamiento_new'),
]