from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import Question
from .forms import AddQuestionForm

def p(*args):
    print(f"***********", *args, sep=" ")



def test(request):
    print("request:", request.GET)
    return HttpResponse(f"<h1>Страница в разработке</h1>"
                        f"requst = {request.GET}"
                        # f"requst = {request}"
                        )



def get_question(request):
    # q = Question.objects.get(id=1)
    q = Question.objects.order_by("?").first()
    con = {
        "title": "question title",
        "q": q,
    }
    return render(request, "know_me/question.html", con)


def create_question(request):
    p("request -", request)
    if request.method == "POST":
        p("POST - ", request.POST)
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_question")
    if request.method == "GET":
        p("GET - ", request.GET)
        form = AddQuestionForm
        con = {
            "title": "добавление вопроса",
            "form": form,
        }
        # return render(request, "know_me/add_question.html")
        return render(request, "know_me/add_question.html", con)


from django.views.generic import ListView


class QuestionList(ListView):
    model = Question
    template_name = "know_me/Question_list_.html"
    context_object_name = "questions"
    extra_context = {"title":"заголовок"}

    def get_queryset(self):
        return Question.objects.filter(question="555")


