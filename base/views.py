from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
                                Q(name__icontains=q)|
                                Q(description__icontains=q))
    topic = Topic.objects.all()[:15]
    
    context = {'rooms':rooms,
                'topic':topic}
    return render(request,'home.html',context=context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    print('this is pk---',request.GET.get('pk'))
    return render(request,'room.html',{'room':room})


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


def update_room(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method  == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect(room.get_absolute_url())
    context = {'form':form}
    return render(request, 'update_room.html', context)


def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request, 'delete.html',{'obj':room})