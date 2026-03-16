from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)
        print (user, username, password)
        if user is not None:
            login(request, user)
            return  redirect('home')
    return render(request, 'login.html')
def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email = email, password=password )
        user.save()
        
        return redirect('login')
    return render(request, 'reg.html')  


