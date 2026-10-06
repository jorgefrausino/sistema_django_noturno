from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), # Correção: Chama o index do CRUD
    path('')

]