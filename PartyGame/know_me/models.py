from django.db import models

# Create your models here.

class Question(models.Model):

    question = models.CharField(max_length=300, verbose_name="вопрос") #, name="вопрос"
    # answer = models.CharField("ответ", max_length=300)

    # def __str__(self):
    #     return str(self.question)



