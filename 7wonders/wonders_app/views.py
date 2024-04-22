from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .forms import BoardForm

# Create your views here.

# home page
def index(request):
   return render(request, 'wonders_app/index.html')

# view to display all of the different students
def boardList(request):
    board_list = Board.objects.all()
    context = {'board_list': board_list}
    return render (request, 'wonders_app/boardList.html', context)

# view to look at the individual details of a board
def boardDetail(request, my_id):
    board_obj = Board.objects.get(id=my_id)
    context = {'board_obj': board_obj}
    return render (request,'wonders_app/boardDetail.html', context)

# view to create a board
def createBoard(request):

    #display default form first time requested
    form = BoardForm()

    if request.method == 'POST':

        # store the data the user entered into a variable
        board_data = request.POST.copy()
        form = BoardForm(board_data)

        if form.is_valid():
            form.save()
            # redirect back to the board list page
            return redirect(boardList)
    
    context = {'form': form}
    return render(request, 'wonders_app/boardForm.html', context)


# view to edit an existing board
def updateBoard(request, my_id):
    # get the correct board object and if the request is post save the
    # data entered in the form
    board_obj = Board.objects.get(id=my_id)
    form = BoardForm(request.POST or None, instance=board_obj)

    if form.is_valid():
        form.save() 
        # redirect back to the portfolio detail page
        return redirect(boardList)
    
    context = {'form': form}
    return render(request, 'wonders_app/boardForm.html', context)

def deleteBoard(request, my_id):
    board_obj = Board.objects.get(id=my_id)

    if request.method == "POST":
        board_obj.delete()
        # redirect back to the portfolio detail page
        return redirect(boardList)
    
    context = {"board_obj": board_obj}
    return render (request,'wonders_app/boardDeleteForm.html', context)

def addCards(request, my_id):
    board_obj = Board.objects.get(id=my_id)

    if request.method == "POST":
        # redirect back to the portfolio detail page
        return redirect(boardDetail(my_id=my_id))
    
    context = {"board_obj": board_obj}
    return render (request,'wonders_app/addCardForm.html', context)

# to be implemented later
def login(request):
    return HttpResponse("login page :)")
def logout(request):
   return HttpResponse("logout")
