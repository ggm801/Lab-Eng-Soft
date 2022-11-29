"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from book import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin', admin.site.urls),
    path('crud', views.crud, name='crud'),
    path('login', views.My_view, name='login'),
    path('relatorio', views.relatorio, name='relatorio'),
    path('atualizarvoo', views.updateflight, name='atualizarvoo'),
    path('formPage', views.vooForm),
    path('relatorioFormPage', views.relatorioForm),
    path('update_voo/<str:pk>', views.vooUpdateForm, name='update_voo'),
    path('delete_voo/<str:pk>', views.deleteVoo, name='delete_voo')

]
