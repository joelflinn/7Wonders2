from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

# home page
def index(request):
   return render(request, 'wonders_app/index.html')

# view to display all of the different students
def boardList(request):
    board_list = Board.objects.all()
    context = {'board_list' : board_list}
    return render (request, 'wonders_app/boardList.html', context)


# to be implemented later
def login(request):
    return HttpResponse("login page :)")
def logout(request):
   return HttpResponse("logout")
