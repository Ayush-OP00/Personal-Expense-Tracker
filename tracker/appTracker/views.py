from django.shortcuts import render, redirect

from django.contrib.auth.models import User

# Create your views here.
def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(name = name, username=username, email = email, password=password )
        user.save()
        
        return redirect('login')
    return render(request, 'reg.html')  
