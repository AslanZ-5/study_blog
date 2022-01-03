from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, "name": 'lets learn python'},
    {'id':2, "name": 'Design with me'},
    {'id':3, "name": 'Front end developers'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request,'home.html',context=context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    print('this is pk---',request.GET.get('pk'))
    return render(request,'room.html',{'room':room})