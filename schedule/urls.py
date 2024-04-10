"""
URL configuration for schedule project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bahia/', views.bahia, name='bahia'),
    path('create/', views.criar_agendamento, name='criar_agendamento'),
    path('list/', views.listar_agendamentos, name='listar_agendamentos'),
    path('confirmar/<int:agendamento_id>/', views.confirmar_agendamento, name='confirmar_agendamento'),
    path('confirmacao/<int:agendamento_id>/', views.pagina_confirmacao, name='pagina_confirmacao'),

]
