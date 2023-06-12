from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView,  DeleteView

from .models import Question, Tag
from .forms import AddQuestionForm

class QuestionList(ListView):
    model = Question
    template_name = "know_me/QuestionList.html"
    context_object_name = "questions"
    extra_context = {"title": "вопросы"}

    def get_queryset(self):
        return Question.objects.filter(tag__name_tag="t1")

class QuestionCreate(CreateView):
    # model = Question
    form_class = AddQuestionForm
    template_name = "know_me/QuestionCreate.html"
    extra_context = {"title": "создание вопроса"}
    success_url = reverse_lazy("home")

class QuestionDetail(DetailView):
    model = Question
    context_object_name = "q"
    template_name = "know_me/QuestionDetail.html"
    extra_context = {"title": "вопрос"}


class QuestionUpdate(UpdateView):
    model = Question
    template_name = "know_me/QuestionUpdate.html"
    # - context_object_name = "form"
    # fields = "__all__"
    fields = ["question",  "tags"]
    success_url = reverse_lazy("home")
    extra_context = {"title": "вопрос"}

class QuestionDelete(DeleteView):
    model = Question
    template_name = "know_me/QuestionDelete.html"
    context_object_name = "q"
    success_url = reverse_lazy("home")
    extra_context = {"title": "вопрос"}










