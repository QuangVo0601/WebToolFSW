# backend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_page),
    path('inputPage/', views.input_list),
    path('inputPage/<int:pk>/', views.input_detail),
]