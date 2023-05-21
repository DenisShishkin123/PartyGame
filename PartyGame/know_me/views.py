from django.shortcuts import render, HttpResponse

# Create your views here.


def test(request):
    print("request:", request.GET)
    return HttpResponse(f"<h1>Страница в разработке</h1>"
                        f"requst = {request.GET}"
                        # f"requst = {request}"
                        )

def get_question(request):

    con = {
        "title": "question title"
    }
    return render(request, "know_me/question.html", con)

