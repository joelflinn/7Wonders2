from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   return render(request, 'wonders_app/index.html')

def login(request):
    return HttpResponse("login page :)")

def logout(request):
   return HttpResponse("logout")
