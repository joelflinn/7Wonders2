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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name']
        exclude = ['user', 'number_of_wins']