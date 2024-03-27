from django.urls import path
from . import views

app_name = 'volumen'

urlpatterns = [
    path('', views.index, name='index'),
    path('calcular/', views.calcular_volumen, name='calcular_volumen'),
]
