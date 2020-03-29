from django.contrib import admin
from django.urls import path
from toc import views

urlpatterns = [
    path('dealer/', views.deal),
    ]