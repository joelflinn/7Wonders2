from django.urls import path
from . import views
from .models import *

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),

path('boards/', views.boardList, name = 'boardList'),
path('board/<int:my_id>', views.boardDetail, name = 'boardDetail'),
path('create_board/',views.createBoard, name = 'createBoard'),
path('update_board/<int:my_id>/', views.updateBoard, name = 'updateBoard'),
path('delete_board/<int:my_id>/', views.deleteBoard, name = 'deleteBoard'),

# to be implemented later
path('login', views.login, name = 'login'),
path('logout',views.logout, name ='logout'),
]
