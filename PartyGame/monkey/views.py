from django.shortcuts import render, HttpResponse



def test(request):
    return render(request, "monkey/test.html", {"title": "заголовок",
                                                "content": "контент"})


