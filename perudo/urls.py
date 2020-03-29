from django.contrib import admin
from django.urls import path
from perudo import views

urlpatterns = [
    path('dealer/', views.deal),
    ]