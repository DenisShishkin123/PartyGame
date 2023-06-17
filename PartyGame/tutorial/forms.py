from django import forms

from .models import Article


# class ArticleForm(forms.BaseModelFormSet ???):
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        # fields = []












