from django.contrib import admin
from django.urls import path, include
from Game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('belote/', include("belote.urls")),
    path('perudo/', include("perudo.urls")),
    path('toc/', include("toc.urls")),
    path('', views.home, name="index"),
]
