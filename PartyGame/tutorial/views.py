from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleForm


def test(request):
    return HttpResponse("test")


def get_article(request, id):
    article = Article.objects.get(pk=id)
    context = {
        "article": article,
    }
    return render(request, "article/ArticleDetail.html", context)


class ArticleDetail(DetailView):
    model = Article
    template_name = "article/ArticleDetail.html"
    context_object_name = "article"
    extra_context = {"title": "заголовок"}


class ArticleList(ListView):
    model = Article
    template_name = "article/ArticleList.html"
    context_object_name = "articles"
    extra_context = {"title": "заголовок"}

    # def get_queryset(self):
    #     return Article.objects.filter(slug="Slug")


# Create
class ArticleAdd(CreateView):
    form_class = ArticleForm
    template_name = "article/ArticleAdd.html"

# Reade
# Update
class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/ArticleAdd.html"
    # success_url = reverse_lazy("test")

# Delete
class ArticleDelete(DeleteView):
    model = Article
    template_name = "article/ArticleDelete.html"
    context_object_name = "article"
    success_url = reverse_lazy("test")


