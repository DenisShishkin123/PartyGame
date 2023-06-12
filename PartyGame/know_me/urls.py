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
from django.urls import path
# from .views import *
from .views import test, get_question, get_question_tag
from .views_class import *

urlpatterns = [
    path("", test, name="test"),
    path("home/", test, name="home"),

    path("QuestionList/", QuestionList.as_view(), name="QuestionList"),
    path("QuestionCreate/", QuestionCreate.as_view(), name="QuestionCreate"),
    path("QuestionDetail/<int:pk>", QuestionDetail.as_view(), name="QuestionDetail"),
    path("QuestionUpdate/<int:pk>", QuestionUpdate.as_view(), name="QuestionUpdate"),
    path("QuestionDelete/<int:pk>", QuestionDelete.as_view(), name="QuestionDelete"),


    # path("q/", get_question, name="get_question"), # get random
    path("q/<tag>/", get_question_tag, name="get_question_tag"), # get random



    #
    # path("q_add/", create_question, name="create_question"), # создать
    # path("q/", get_question, name="question"), # get random
    # path("q_detail/<id>", deteil_question, name="q_detail"),
    #
    # # ClassView
    # path("q_create_/", CreateQuestion.as_view(), name="CreateQuestion"),
    #
    # path("q_create_c", QuestionCreate.as_view(), name="QuestionCreate"),
    # path("q_list_c/", QuestionList.as_view(), name="QuestionList"),
    # path("q_detail_c/<pk>", QuestionDetail.as_view(), name="QuestionDetail"),
    #
    #
    #
    # path("q_add_list/", AddQuestionList.as_view(), name="AddQuestionList"),
    #
    #
    # # test  для студента
    # path("add_test/", add_test, name="add_test")
]



