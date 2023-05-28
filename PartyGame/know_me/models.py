from django.db import models

# Create your models here.

class Question(models.Model):

    question = models.CharField(max_length=300, verbose_name="вопрос") #, name="вопрос"
    # answer = models.CharField("ответ", max_length=300)
    tag = models.CharField(max_length=100, blank=True, verbose_name="tag")

    def __str__(self):
        return self.question



