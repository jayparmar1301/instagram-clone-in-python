from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Posts

@login_required(login_url='login')
def hello(request):
    return HttpResponse('Hello, Welcome to my Instagram Clone.')

@login_required
def detail(request, id):
    try:
        user_obj = Posts.objects.get(id = id)
        print(user_obj.user_name, user_obj.caption)

        return HttpResponse(f'Welcome back {user_obj}')
    
    except:
        return HttpResponse('You Dont have any post yet')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']        
            
        user = authenticate(request, username=username, password=password)
        u = User.objects.get(username=username)
        
        if user is not None:
            login(request, user)
            return redirect('detail', id = u.id)
        else:
            # Authentication failed, show an error message
            error_message = "Invalid username or password."
            return render(request, 'registration/login.html', {'error_message': error_message})
    
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
        
    return render(request, 'registration/signup.html')

def user_logout(request):
    logout(request)
    return redirect('login')