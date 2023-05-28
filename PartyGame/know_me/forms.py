from django import forms

from .models import Question

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        # fields = ["question", "answer"]


class AddQuestionListForm(forms.Form):
    sep = forms.CharField( max_length=5, label="разделитель")
    name = forms.CharField(max_length=50, label="название колоды")
    info = forms.CharField(max_length=500, label="анатация колоды")
    text = forms.CharField(max_length=5000, label="данные")
    # file = forms.CharField(max_length=5000, label="данные")
    tag = forms.CharField(max_length=100, label="тег", required=False)
    # tag = forms.ModelChoiceField(queryset=Category.objects.all(), label="тип вопроса")
    type = forms.CharField(max_length=100, label="тип")
    # type = forms.ModelChoiceField(queryset=Category.objects.all(), label="тип вопроса")
    is_published = forms.BooleanField(initial=True, label="Публикация")


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label="Заголовок")
#     slug = forms.SlugField(max_length=255, label="URL")
#     content = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
#     is_published = forms.BooleanField(initial=True, label="Публикация")
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории")

# Теперь, все выглядит гораздо приятнее.
# Давайте для примера сделаем поле content необязательным,
# а поле is_published с установленной галочкой.
# Соответственно, в классе CharField пропишем параметр required=False,
# а в классе BooleanField – параметр initial=True.
# Еще в классе ModelChoiceField добавим параметр empty_label="Категория не выбрана",
# чтобы вместо черточек отображалась по умолчанию в списке эта фраза.

