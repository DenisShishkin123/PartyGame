from django import forms

from .models import Card

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = "__all__"
        


class StartForm(forms.Form):
    # Игра
    # число игроков
    quantity_of_players = forms.IntegerField()
    # номер комноты / число для рандома
