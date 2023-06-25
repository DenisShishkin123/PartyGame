from django.shortcuts import render, HttpResponse



def test(request):
    return render(request, "monkey/test.html", {"title": "заголовок",
                                                "content": "контент"})


def get_random(request):
    # card = Card.objects.get(pk=1)
    card = Card.objects.order_by("?").first()
    con = {
        "title": "заголовок",
        "c": card
    }
    return render(request, "monkey/action.html", con)



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Card
from .forms import CardForm

class CardList(ListView):
    model = Card
    template_name = "monkey/CardList.html"
    context_object_name = "cards"
    extra_context = {"title": "заголовок"}


class CardDetail(DetailView):
    model = Card
    template_name = "monkey/CardDetail.html"
    context_object_name = "c"
    extra_context = {"title": "заголовок"}

class CardCreate(CreateView):
    form_class = CardForm
    template_name = "monkey/CardCreate.html"
    # context_object_name = "form"
    extra_context = {"title": "заголовок"}


class CardUpdate(UpdateView):
    model = Card
    fields = "__all__"
    # form_class = CardForm
    template_name = "monkey/CardCreate.html"
    # context_object_name = "form"
    extra_context = {"title": "заголовок"}


class CardDelete(DeleteView):
    model = Card
    template_name = "monkey/CardDelete.html"
    context_object_name = "c"
    extra_context = {"title": "заголовок"}
    success_url = reverse_lazy("test")






