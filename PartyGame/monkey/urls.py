"""
URL configuration for PartyGame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import *

urlpatterns = [
    # test
    path("s", session_start, name="session"),
    path("test", test, name="m_test"),

    # play
    path("start/", start, name="start"),
    path("play/", play, name="play"),



    # get random
    path("", get_random, name="random"),

    # CRUD
    path("list", CardList.as_view(), name="CardList"),
    path("card/<int:pk>", CardDetail.as_view(), name="card"),
    path("card/delete/<int:pk>", CardDelete.as_view(), name="delete"),
    path("card/update/<int:pk>", CardUpdate.as_view(), name="update"),
    path("card/create", CardCreate.as_view(), name="create"),

]
