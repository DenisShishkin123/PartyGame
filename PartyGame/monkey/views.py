import random

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy

from .forms import StartForm
"""
# ******************************  test  ****************************** #
"""

def p(value, key=None):
    print(f"******** {key} -- {value}")

def session_start(request):
    request.session["test"] = 0
    request.session["d"] = {
        "0": 0,
        "2": 2,
    }
    return redirect("m_test")
    # return reverse_lazy("m_test")


def test(request):

    # request.session["test"] = 0
    request.session["test"] += 1
    request.session["d"]["0"] += 1
    request.session["d"]["1"] = 1
    session = request.session["test"]
    d = request.session["d"]

    return render(request, "monkey/test.html", {"title": "заголовок",
                                                # "content": "контент"})
                                                "content": f"{session} - {d}"})



def get_random(request):
    # card = Card.objects.get(pk=1)
    card = Card.objects.order_by("?").first()
    con = {
        "title": "заголовок",
        "c": card
    }
    return render(request, "monkey/action.html", con)


"""
# ******************************  PLAY  ****************************** #
"""


def start(request):
    if request.method == "POST":
        # формирует сессию
        p(request, "request")
        p(request.POST, "request.POST")
        p(request, "request")

        n = request.POST["quantity_of_players"][0]
        if n:
            request.session["quantity_of_players"] = int(n)
            request.session["number_players"] = int(n)  # или 0
            request.session['card'] = ''

        form = StartForm(request.POST)
        return redirect("play")

    else:
        # выводит форму для заполнения
        form = StartForm()
    con = {
        "title": "start monkey",
        "form": form,
    }
    return render(request, "monkey/Form.html", con)


def play(request):

    def next(request):
        if request.session['number_players'] in request.session['namber_monkey']:
            card = "you monkey"
        else:
            card = request.session['card']
        con = {
            "title": "monkey",
            "card": card,
            "number_players": request.session['number_players'],
            "quantity_of_players": request.session['quantity_of_players'],

            # "number": f"{request.session['number_players']} / {request.session['quantity_of_players']}",
            # "end": request.session['number_players'] == 1
        }
        request.session['number_players'] -= 1
        return render(request, "monkey/play.html", con)

        # response = HttpResponse(
        #     f"{request.session['number_players']} / {request.session['quantity_of_players']} <br>"
        #     f"{card}"
        #     # f"<form action='{{% url 'play' %}}'> <button>next</button> </form>"
        # )
        # return response




    def play_start(request):
        # p('play_start')
        n = request.session['quantity_of_players']
        request.session["number_players"] = n  # или 0
        request.session["namber_monkey"] = [random.randint(1, n)]


        card = Card.objects.order_by("?").first()
        request.session['card'] = card.action
        # request.session['card'] = "card.action"

        return next(request)

    if request.session["number_players"] == 0 or not request.session['card']:
        return play_start(request)
    else:
        return next(request)


# вводится количество играков
# генерируется раунд : выбирается рандомная карточка + в сессии сбрасывается номер игрока
# по кругу
#     экран игрока № n (посмотреть вопрос , передать следующему) - кнопка next
#     экран последнего - кнопка next раунд



"""
# ******************************  CRUDE  ****************************** #
"""



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






