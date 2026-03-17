from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.db.models import Sum
from django.db.models.functions import TruncMonth


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
    
# Data_Visualization
def data_visualization(request):

    expenses = Expense.objects.all()

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

    total_income = 0

    balance = total_income - total_expense

    context = {
        'expenses':expenses,
        'monthly_data':monthly_data,
        'total_expense':total_expense,
        'total_income': total_income,
        'balance': balance,
    }
    return render(request,'dataVisualization.html', context)

