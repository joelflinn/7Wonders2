from django.forms import ModelForm
from .models import Board
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# create class for board form
class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ('name','board_type','win_or_loss','score', )