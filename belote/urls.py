from django.contrib import admin
from django.urls import path
from belote import views

urlpatterns = [
    path('', views.dealer, name="belote"),
    path('<str:name>/cartes', views.dealer, name="name-belote"),
    path('newdeal/', views.new_deal, name="newdeal-belote")
    ]