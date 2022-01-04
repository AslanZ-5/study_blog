from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User                      
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout 


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('base:home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"This user doesn't exists")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base:home')
        else:
            messages.error(request, "Username or password does not exists")

    context = {'page':page}
    return render(request,'login_register.html',context)

def logout_user(request):
    logout(request)
    return redirect('base:home')

def register_page(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('base:home')
        else:
            messages.error(request, 'An error eccured during registration')

    return render(request, 'login_register.html',{'form':form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
                                Q(name__icontains=q)|
                                Q(description__icontains=q))
    topic = Topic.objects.all()[:15]
    room_count = rooms.count()
    context = {'rooms':rooms,
                'topic':topic,
                'room_count':room_count}
    return render(request,'home.html',context=context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()
    context = {
        'room':room,
        'messages':messages,
    }    
    return render(request,'room.html',context)

@login_required(login_url='base:login')
def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
        print(request.POST)
    context = {'form':form}
    return render(request,'room_form.html',context)


@login_required(login_url='base:login')
def update_room(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('You are not allowed here! Only room authors can to update info.')
    if request.method  == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect(room.get_absolute_url())
    context = {'form':form}
    return render(request, 'update_room.html', context)

@login_required(login_url='base:login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here! Only room authors can to update info.')
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request, 'delete.html',{'obj':room})


