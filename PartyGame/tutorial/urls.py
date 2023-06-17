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

from django.urls import path
from .views import *

# http://127.0.0.1:8000/tutorial/

urlpatterns = [
    path("", test, name="tutorial"),
    # path("<int:id>", get_article, name="article"),

    # path("<int:pk>", ArticleDetail.as_view(), name="article_detail"),
    path("<slug:slug>", ArticleDetail.as_view(), name="article_detail"),
    path("list/", ArticleList.as_view(), name="article_list"),
    path("add/", ArticleAdd.as_view(), name="article_add"),
    path("update/<int:pk>", ArticleUpdate.as_view(), name="article_update"),
    path("delete/<int:pk>", ArticleDelete.as_view(), name="article_delete"),
]
