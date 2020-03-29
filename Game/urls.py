from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('belote/', include("belote.urls")),
    path('perudo/', include("perudo.urls")),
    path('toc/', include("toc.urls")),
]
