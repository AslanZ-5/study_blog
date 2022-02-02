from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Message, Room, Topic,Profile
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User                      
from django.contrib import messages
from django.core.paginator import Paginator



def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
                                Q(name__icontains=q)|
                                Q(description__icontains=q))
    
    paginator = Paginator(rooms,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    topic = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))[:7]
    context = {
                'topic':topic,
                'room_count':room_count,
                'room_messages':room_messages,
                'page_obj':page_obj
                }
    
    return render(request,'home.html',context=context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room=room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('base:room',pk=room.id)
    context = {
        'room':room,
        'messages':messages,
        'participants':participants,
    }    
    return render(request,'room.html',context)



@login_required(login_url='users:login')
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == "POST":
        topic,created = Topic.objects.get_or_create(name=request.POST.get('topic')) 
        a = Room.objects.create(
            name= request.POST.get('name'),
            host= request.user,
            description= request.POST.get('description'),
            topic= topic,
        )
        return redirect(a.get_absolute_url())
        
            

    context = {'form':form,'topics':topics}
    return render(request,'create-room.html',context)


@login_required(login_url='base:login')
def update_room(request,pk):
    topics = Topic.objects.all()
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('You are not allowed here! Only room authors can to update info.')
    if request.method  == "POST":
       
        topic,created = Topic.objects.get_or_create(name=request.POST.get('topic')) 
        room.topic = topic
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.save()
        return redirect(room.get_absolute_url())
    context = {'form':form,'topics':topics,'room':room}
    return render(request, 'create_update_room.html', context)

@login_required(login_url='base:login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here! Only room authors can to delete room .')
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request, 'delete.html',{'obj':room})


@login_required(login_url='base:login')
def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here! Only message authors can to delete message.')
    if request.method == 'POST':
        message.delete()
        return redirect('base:home')
    return render(request, 'delete.html',{'obj':message})




def topics_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    topics = Topic.objects.filter(name__icontains=q)
    context = {'topics':topics}
    return render(request,'topics.html',context=context)


def activities_view(request):
    messages = Message.objects.all()[:6]
    context = {'messages':messages}
    return render(request,'activity.html',context=context)