from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from django.db.models import Sum
from django.db.models.functions import TruncMonth


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # print("USERNAME:", username)
        # print("PASSWORD:", password)

        user = User.objects.create_user(username=username, password=password)
        # print("USER:", user)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard') #this is key
        else:
           return render(request, 'login.html',{'error': 'Invalid username or password'})
    return render(request, 'login.html')
def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'reg.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email = email, password=password )
        user.save()
        
        return redirect('login')
    return render(request, 'reg.html')  

@login_required
def manage_expenses(request):

    if request.method == "POST":
        if 'income_submit' in request.POST: 
            amount = request.POST.get('income')
            Income.objects.create(user = request.user, amount=amount)
        else:
            title=request.POST.get('title')
            amount=request.POST.get('amount')
            category=request.POST.get('category')
            date=request.POST.get('date')

            Expense.objects.create(user = request.user, title=title, amount=amount, category=category, date=date)
        return redirect('manage')
    # only logged-in user's data'
    expenses = Expense.objects.filter(user = request.user)
    incomes = Income.objects.filter(user = request.user)

    total_income = sum([i.amount for i in incomes])

    return render(request, 'manage.html', {'expenses':expenses, 'total_income': total_income})

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
    
# Data_Visualization
@login_required
def data_visualization(request):

    expenses = Expense.objects.filter(user=request.user)

    #Filter Logic
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if category: expenses = expenses.filter(category=category)

    if start_date: expenses = expenses.filter(date_gte=start_date)

    if end_date: expenses = expenses.filter(date_lte=end_date)

    # MONTHLY SUMMARY
    monthly_data = (expenses.annotate(month=TruncMonth('date'))
                    .values('month')
                    .annotate(total=Sum('amount'))
                    .order_by('month'))

    # TOTAL CALCULATIONS
    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0

    total_income = Income.objects.filter(user = request.user)\
        .aggregate(total=Sum('amount'))['total'] or 0

    balance = total_income - total_expense

    context = {
        'expenses':expenses,
        'monthly_data':monthly_data,
        'total_expense':total_expense,
        'total_income': total_income,
        'balance': balance,
    }
    return render(request,'dataVisualization.html', context)

# LOGOUT FUNCTION
def logout_view(request):
    logout(request)
    return redirect('login')

