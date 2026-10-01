from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), # Aqui sim chama o login
    path('novo-usuario/', views.novo_usuario, name='novo_usuario'),
]