from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import ListView

# Create your views here.
from .models import Question
from .forms import AddQuestionForm, AddQuestionListForm


'''
'''
from .models import Tag, Question
from .forms import Tag_Question_Form


def form(request, error=None):
    form = Tag_Question_Form()
    con = {
        "form": form,
        "error": error,
    }
    return render(request, "know_me/add_test.html", con)


def add_test(request):
    if request.method == "POST":
        print(f"******** request.POST - {request.POST}")
        # print(f"******** request.POST['name_tag'] - {request.POST['name_tag']}")
        # print(f"******** request.POST['name_tag'] - {type(request.POST['name_tag'])}")
        try:
            try:
                tag = Tag.objects.get(name_tag=request.POST["name_tag"])
            except Tag.DoesNotExist:
                tag = Tag.objects.create(name_tag=request.POST["name_tag"])

            Question.objects.create(tag=tag, question=request.POST["question"])
        except Exception:
            return form(request, error="УПС")

        return form(request, error="сохранилось")

    else:
        return form(request)

    # tag_id = tag.id
    # tag = Tag(name_tag=request.POST["name_tag"][])

    # if tag.is_valid():
    #     tag.save()
    #
    #     question = Question(tag=tag , question=request.POST["question"][])
    #     if question.is_valid():
    #         question.save()








'''
'''


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
            p(" form.cleaned_data - ", form.cleaned_data)
            form.save()
        return redirect("create_question")
    if request.method == "GET":
        p("GET - ", request.GET)
        form = AddQuestionForm()
        con = {
            "title": "добавление вопроса",
            "form": form,
        }
        # return render(request, "know_me/add_question.html")
        return render(request, "know_me/add_question.html", con)


def parser(data_in):
    sep = data_in["sep"]
    text = data_in["text"]
    data_res = text.split(sep)
    p(data_res)
    return data_res

def save_list_q(list, model):
    for q in list:
        p(q)
        qq = model.objects.create(question=q)
        p(qq)

def parser_save(data_in, model):
    data_list = parser(data_in)
    save_list_q(data_list, model)


class AddQuestionList(View):
    def get(self, request):
        # p("request -", request)
        # p("GET - ", request.GET)
        form = AddQuestionListForm()
        p(" form - ", form)
        con = {
            "title": "добавление вопроса",
            "form": form,
        }
        return render(request, "know_me/add_question.html", con)
    def post(self, request):
        p("request -", request)
        p("POST - ", request.POST)
        form = AddQuestionListForm(request.POST)
        if form.is_valid():
            p(" form - ", form)
            p(" form.cleaned_data - ", form.cleaned_data)
            p(" form.cleaned_data - ", *form.cleaned_data.values())
            p(" form.cleaned_data - ", form.cleaned_data['sep'])
            # form.save()
        # return redirect("create_question")
            try:
                p("try")
                p(type(form.cleaned_data))
                parser_save(dict(form.cleaned_data), Question)

                # Question.objects.create(**form.cleaner_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
                p("ERROR")
                return redirect('AddQuestionList')








class QuestionList(ListView):
    model = Question
    template_name = "know_me/Question_list_.html"
    context_object_name = "questions"
    extra_context = {"title":"заголовок"}

    def get_queryset(self):
        return Question.objects.filter(question="555")


