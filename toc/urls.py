from django.contrib import admin
from django.urls import path
from toc import views

urlpatterns = [
    path('', views.dealer, name="toc"),
    path('<int:tour>/', views.dealer, name="toc-tour"),
    path('<str:name>/cartes', views.player, name="name-toc"),
    path('newdeal/', views.new_deal, name="newdeal-toc")
    ]