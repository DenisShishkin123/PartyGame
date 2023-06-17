from django.db import models
from django.urls import reverse, reverse_lazy


class Article(models.Model):
    # article
    slug = models.SlugField(unique=True, db_index=True)
    # slug = models.CharField("слаг", max_length=50)

    title = models.CharField(max_length=50, verbose_name="название")
    # body = models.CharField(max_length=500, verbose_name="содержание")
    # content -  подключить редактор в админку, как вставлять картинки в ткст и примеры кода
    text = models.TextField("содержание")

    datetime_add = models.DateTimeField(auto_now_add=True)
    datetime_edit = models.DateTimeField(auto_now=True)
    # author =
    # tag =
    # tags =


    def __str__(self):
        return self.title

        # get_absolute_url
    def get_absolute_url(self):
        # return f"{self.slug}"
        # return reverse("article_detail", args=[str(self.id)])
        return reverse("article_detail", kwargs={"slug": self.slug})













