"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from SGDR.views import index_agenda, index_criacao, index_info, update_contato, delete_contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', index_agenda, name = "index"),
    path('criacao/', index_criacao, name = "index_criacao"),
    path('contato/<int:id_contato>', index_info, name = "index_info"),
    path('update/<int:id_contato>', update_contato, name = "update_contato"),
    path('delete/<int:id_contato>', delete_contato, name = "delete_contato"),
    
]
