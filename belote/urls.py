from django.contrib import admin
from django.urls import path
from belote import views

urlpatterns = [
    path('dealer/', views.dealer, name="dealer"),
    path('<str:name>/', views.dealer, name="name"),
    path('dealer/newdeal/', views.new_deal, name="newdeal")
    ]