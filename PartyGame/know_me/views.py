from django.shortcuts import render, HttpResponse

# Create your views here.


def test(request):
    print("request:", request.GET)
    return HttpResponse(f"<h1>Страница в разработке</h1>"
                        f"requst = {request.GET}"
                        # f"requst = {request}"
                        )

from .models import Question

def get_question(request):
    # q = Question.objects.get(id=1)
    q = Question.objects.order_by("?").first()
    con = {
        "title": "question title",
        "q": q,
    }
    return render(request, "know_me/question.html", con)

