from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from base.models import Message, Room, Topic,Profile
from .forms import UserForm,ProfileForm,RegistrationForm
from django.db.models import Q
from django.contrib.auth.models import User                      
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class PasswordsChangeView(PasswordChangeView):
    success_url = reverse_lazy('users:password_success')
    template_name = 'change-password.html'

def password_success(request):
    return render(request, 'users/password_success.html')

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('blog:home')
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
            return redirect('blog:home')
        else:
            messages.error(request, "Username or password does not exists")

    context = {'page':page}
    return render(request,'login_register.html',context)

def logout_user(request):
    logout(request)
    return redirect('blog:home')

def register_page(request):
    
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('blog:home')
        else:
            messages.error(request, 'An error eccured during registration')
            return render(request, 'login_register.html',{'form':form},status=400)

    return render(request, 'login_register.html',{'form':form})





def userProfile(request,pk):
    profile = Profile.objects.get(user_id=pk)
    rooms = profile.user.room_set.all()
    topic = Topic.objects.all()
    room_messages = profile.user.message_set.all()
    context = {
                'rooms':rooms,
                'topic':topic,
                'room_messages':room_messages,
                'profile':profile,
                }
    return render(request, 'profile.html',context=context)



@login_required(login_url='login')
def editUser(request,pk):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = UserForm(instance=user)
    P_form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        P_form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid() and P_form.is_valid():
            form.save()
            P_form.save()
            return redirect('users:user-profile',user.id)
    

    return render(request,'edit-user.html',{'form':form,'pform':P_form})