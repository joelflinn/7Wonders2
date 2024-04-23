from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# create class for board form
class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ('name','board_type','win_or_loss','score', )

'''
class AddCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('card_image',)
'''

class CardForm(forms.Form):

    CARDS = (
    ('Well','Well'),
    ('Baths','Baths'),
    ('Altar','Altar'),
    ('Theater','Theater'),
    ('Statue','Statue'),
    ('Aqueduct','Aqueduct'),
    ('Temple','Temple'),
    ('Courthouse','Courthouse'),
    ('Pantheon','Pantheon'),
    ('Gardens','Gardens'),
    ('Townhall','Townhall'),
    ('Palace','Palace'),
    ('Senate','Senate'),
    )

    my_card_choices = forms.ChoiceField(choices=CARDS, widget 
    =forms.RadioSelect())