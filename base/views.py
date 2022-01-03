from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'home.html',context=context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    print('this is pk---',request.GET.get('pk'))
    return render(request,'room.html',{'room':room})