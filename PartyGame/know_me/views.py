from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

# Create your views here.
from .models import Question, Tag
# from know_me.models import Question, Tag
from .forms import AddQuestionForm, AddQuestionListForm



def p(*args):
    print(f"***********", *args, sep=" ")


def test(HttpRequest):
    # print("*"*50)
    # print("request:", HttpRequest.GET)
    # print("body:", HttpRequest.body)
    # print("read:", HttpRequest.read())
    # print("request:", HttpRequest.POST)
    return HttpResponse(f"<h1>Страница в разработке</h1>"
                        f"<a href='https://django.fun/ru/docs/django/4.1/ref/request-response/'>  подробнее про request </a><br>"
                        f"<p>HttpRequest.GET = {HttpRequest.GET}</p>"
                        f"HttpRequest.path = {HttpRequest.path}"
                        f"HttpRequest.method = {HttpRequest.method}"
                        f"HttpRequest.content_type = {HttpRequest.content_type}"
                        f"HttpRequest.content_params = {HttpRequest.content_params}"
                        f"HttpRequest.COOKIES = {HttpRequest.COOKIES}"
                        # f"requst = {HttpRequest}"
                        # f"requst = {HttpRequest}"
                        # f"requst = {HttpRequest}"
                        )


def get_question(request):
    # q = Question.objects.get(id=1)
    ''' стандарт '''
    q = Question.objects.order_by("?").first()
    con = {
        "title": "question title",
        "q": q,
    }
    return render(request, "know_me/get_question.html", con)



def get_question_tag(request, tag):
    p(tag)
    q = Question.objects.filter(tag__name_tag=tag).order_by("?").first()
    con = {
        "title": "question title",
        "q": q,
    }
    return render(request, "know_me/get_question.html", con)

"""
def get_question(request):
    # q = Question.objects.get(id=1)
    ''' стандарт '''
    q = Question.objects.order_by("?").first()

    # t = Tag.objects.get(name_tag="tag1")
    # q = Question.objects.filter(tag=t).order_by("?").first()
    # или
    # q = Question.objects.filter(tag__name_tag="t1").order_by("?").first()
    # .distinct().
    # t1 = Tag.objects.get(name_tag="t1")
    # t2 = Tag.objects.get(name_tag="t2")
    # q2 = Question.objects.filter(tags__in=[t1, t2])

    # q2 = Question.objects.filter(tags__in=[1, 2]) # "or"  - если есть или то или то
    # # <QuerySet [<Question: m>, <Question: tt>, <Question: t>, <Question: m>, <Question: tt>]>
    #
    # q2 = Question.objects.filter(tags__in=[1]) & Question.objects.filter(tags__in=[2])
    # # < QuerySet[ < Question: m >, < Question: tt >] >

    # q2 = Question.objects.filter(question="q1", tag_id=2) # & Question.objects.filter( tag_id=2)


    '''  с фильтрами по тегам и тегамс '''
    # # Q = Question.objects.filter(tag__name_tag="t1").filter(tags__name_tag="t1")
    # Q = Question.objects.filter(tag__name_tag="t1")
    # tags = ["t1", "t2"]
    # if tags:
    #     for tag in tags:
    #         # Q.filter(tags__in=[2])
    #         Q = Q.filter(tags__name_teg=tag)
    # q=Q.order_by("?").first()

    con = {
        "title": "question title",
        "q": q,
    }
    return render(request, "know_me/get_question.html", con)
"""

def create_question(request):
    # p("request -", request)
    if request.method == "POST":
        # p("POST - ", request.POST)
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            # p(" form.cleaned_data - ", form.cleaned_data)
            form.save()
        return redirect("create_question")
    if request.method == "GET":
        # p("GET - ", request.GET)
        form = AddQuestionForm()
        con = {
            "title": "добавление вопроса",
            "form": form,
        }
        # return render(request, "know_me/add_question.html")
        return render(request, "know_me/add_question.html", con)




from django.views import View



class CreateQuestion(View):
    form_class = AddQuestionForm
    templates = "know_me/create_Question.html"
    # initial = {'key': 'value'}
    # initial = {'question': 'вашь вопрос'}

    def get(self, request):
        # form = self.form_class(initial=self.initial)
        form = self.form_class
        return render(request, self.templates, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_question_class")
        return render(request, self.templates, {"form": form, "error": "error"})
        # return HttpResponse("error")



from django.views.generic import ListView

class QuestionList(ListView):
    model = Question
    template_name = "know_me/question_list.html"
    # template_name = "know_me/Question_list_.html"
    context_object_name = "questions"
    extra_context = {"title": "заголовок"}

    def get_queryset(self):
        return Question.objects.filter(tag__name_tag="t1")





def deteil_question(request, id):
    # p(id)
    q = Question.objects.get(pk=id)
    return render(request, "know_me/Question.html", {"q": q})



from django.views.generic import DetailView

class QuestionDetail(DetailView):
    model = Question
    template_name = "know_me/Question.html"
    context_object_name = "q"
    extra_context = {"title": f"вопрос      "}


from django.views.generic import CreateView
# from django import revers_lazy


class QuestionCreate(CreateView):
    form_class = AddQuestionForm
    template_name = "know_me/create_Question.html"
    # template_name = "know_me/QuestionAdd.html"
    success_url = reverse_lazy("home")











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













# ******************************************************************* #

'''
# test  для студента
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
