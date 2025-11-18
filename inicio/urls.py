from django.urls import path
from inicio.views import *

urlpatterns = [
    path('', inicio),
    path('crear-colectividad/<nombre>/<pais>/', crear_colectividad)
]
