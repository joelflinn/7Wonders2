from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# decorators
class boardListView(LoginRequiredMixin, generic.ListView):
    model = Board

class boardDetail(LoginRequiredMixin, generic.DetailView):
    model = Board




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

    # var to calculate the total points of the board
    total = 0

    board_obj = Board.objects.get(id=my_id)
    instance_card_list = InstanceCards.objects.all().filter(board_id = my_id)
    context = {'board_obj': board_obj, 'instance_card_list': instance_card_list}

    for card in instance_card_list:
        total = total + card.pointValue

    board_obj.score = total
    board_obj.save()

    return render (request,'wonders_app/boardDetail.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['player_role'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['player_role'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['player_role'])
def deleteBoard(request, my_id):
    board_obj = Board.objects.get(id=my_id)

    if request.method == "POST":
        board_obj.delete()
        # redirect back to the portfolio detail page
        return redirect(boardList)
    
    context = {"board_obj": board_obj}
    return render (request,'wonders_app/boardDeleteForm.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['player_role'])
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

# used to create a user
def registerPage(request):

    form = UserCreationForm()

    if request.method == "POST":
        form_data = request.POST.copy()
        form = UserCreationForm(form_data)

        if form.is_valid():
            print("form was saved")

            userForm = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='player_role')
            print("group was saved")

            userForm.groups.add(group)
            
            # create a player and link the player to the newly created user
            player = Player.objects.create(user=userForm)
            player.name = username
            player.save()
            print("player object was not saved")


            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form' : form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['player_role'])
def userPage(request):
    player = request.user.player
    form = PlayerForm(instance=player)
    print('player', player)

    if request.method=='POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect(boardList)


    context = {'form':form}

    return render(request, 'wonders_app/user.html', context)


# to be implemented later
'''
def login(request):
    return render(request, 'wonders_app/index.html')
    return HttpResponse("login page :)")

def logout(request):
   return HttpResponse("logout")

'''
