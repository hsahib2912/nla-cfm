from django.contrib import admin
from django.urls import path
from login import views
from . import views

urlpatterns = [
    path('',views.login , name = 'login'),
    path('symptoms/', views.select_symptoms),
    path('symptoms/pricing/', views.pricing),
]
