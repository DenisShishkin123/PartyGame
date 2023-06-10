from django.db import models

# Create your models here.

class Tag(models.Model):
    name_tag = models.CharField(max_length=15, verbose_name="тег")

    def __str__(self):
        return self.name_tag



class Question(models.Model):

    question = models.CharField(max_length=300, verbose_name="вопрос") #, name="вопрос"
    # answer = models.CharField("ответ", max_length=300)
    # tag = models.CharField(max_length=100, blank=True, verbose_name="tag")
    tag = models.ForeignKey("Tag", verbose_name="tag", blank=True, on_delete=models.PROTECT
                            , related_name='+',)
    tags = models.ManyToManyField("Tag", verbose_name="tags", blank=True)


    def __str__(self):
        return self.question



