# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PartyGame.settings')
# django.setup()
#
# import os
# import sys
# from django.conf import settings
#
# settings.configure()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PartyGame.settings")
# sys.path.append(BASE_DIR)

# from project_name.wsgi import *
# from PartyGame.wsgi import *

# CRUDE model
# from .models import Question
# from .models import Question
# from models import Question
# from know_me.models import Question


'''
p = Question.objects.get(id=1)
print(p)

#
python manage.py shell # exit
from know_me.models import Question

Question(question="question0", tag="tag0")
w1 = _ # ‘_’ – это специальная ссылка, в которой сохраняется результат последней операции.
w1.save()
w1.question

from django.db import connection
connection.queries


# objects

w4 = Women.objects.create(title='Ума Турман', content='Биография Ума Турман') # сразу сохраняет
w4.pk


Question.objects.all()
Question.objects.filter(tag="old")
Question.objects.get(id=1)
Question.objects.filter(tag="old").order_by('-id')
Question.objects.order_by('-id')

Question.objects.order_by('?').first() # random

q=Question.objects.get(id=1)
q.tag="now"
q.save()
q.delete()


'''

def parser(data_in):
    sep = data_in.sep
    text = data_in.text
    data_res = text.split(sep)
    p(data_res)
    return data_res

sep = "."
text = "data_in.text"
p = text.split(sep)
print(p)



