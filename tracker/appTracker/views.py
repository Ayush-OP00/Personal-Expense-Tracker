from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .models import Expense

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)
        print (user, username, password)
        if user is not None:
            login(request, user)
            return  redirect('manage')
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

def manage_expenses(request):

    if request.method == "POST":
        title=request.POST.get('title')
        amount=request.POST.get('amount')
        category=request.POST.get('category')
        date=request.POST.get('date')

        Expense.objects.create(title=title, amount=amount, category=category, date=date)
        return redirect('manage')
    expenses = Expense.objects.all()
    return render(request, 'manage.html', {'expenses':expenses})

# edit expense

def edit_expense(request, id):
    expense =  get_object_or_404(Expense, id=id)

    if request.method=="POST":
        expense.title = request.POST.get('title')
        expense.amount = request.POST.get('amount')
        expense.category = request.POST.get('category')
        expense.date = request.POST.get('date')

        expense.save()

        return redirect('manage')
    return render(request,'edit_expense.html', {'expense' : expense})

# Delete Expense

def delete_expense(request, id):

    expense = get_object_or_404(Expense, id=id)

    expense.delete()

    return redirect('manage')
    