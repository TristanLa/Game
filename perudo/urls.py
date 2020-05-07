from django.urls import path
from perudo import views

urlpatterns = [
    path('', views.newgame, name="perudo"),
    path('newgame/', views.newgame, name="newgame"),
    path('lost/', views.lost, name="lost"),
    path('won/', views.win, name="won"),
    path('game/<int:dice_number>/', views.game, name="game"),
    ]