from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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
    card_options = Card.objects.all()

    if request.method == "POST":
        # select the items that have a checked box. NOTE: that these items
        # are selected and returned by their pk value in the Card table
        Selected_card_list = request.POST.getlist('boxes')
        print(Selected_card_list)

        # create objects based off the list and store them in a list of objects
        for i in Selected_card_list:
            # card_obj will act as a template for creating the instanceCard object
            # that is assigned to a specific board.
            card_obj = Card.objects.get(id=i)
            # creating an instanceCards object based off info of Card object
            # that was selected
            temp = InstanceCards(
                name = card_obj.name,
                pointValue = card_obj.pointValue,
                board_id = my_id,
                card_image = card_obj.card_image,
            )
            # link those objects to the current board
            temp.save()

        # redirect back to the board detail page
        return redirect(boardList)
    
    context = {"card_options": card_options}
    return render (request,'wonders_app/addCardForm.html', context)

# to be implemented later
def login(request):
    return HttpResponse("login page :)")

def logout(request):
   return HttpResponse("logout")


