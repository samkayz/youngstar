"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', include('user.urls')),
    path('', views.index, name='index'),
    path('add', views.add_question, name='add_question'),
    path('process', views.process, name='process'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit_question, name='edit_question'),
    path('update', views.update_question, name='update_question'),
    path('add_story', views.add_story, name='add_story'),
    path('delete_story/<id>', views.delete_story, name='delete_story'),
]
