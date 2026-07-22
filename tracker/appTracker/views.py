from urllib import request

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.contrib import messages
from appTracker.models import Expense, Income


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # print("USERNAME:", username)
        # print("PASSWORD:", password)

        user = authenticate(
            request, 
            username = username, 
            password = password)
        # print("USER:", user)
        
        if user is not None:
            login(request, user)
            return redirect('manage') #this is key
        else:
           return render(request,
                          'accounts/login.html',
                          {'error': 'Invalid username or password'}
                          )
    return render(request, 'accounts/login.html')

def registration(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            return render(
                request,
                "accounts/register.html",
                {"error": "Passwords do not match."}
            )

        if User.objects.filter(username=username).exists():

            return render(
                request,
                "accounts/register.html",
                {"error": "Username already exists."}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully! Please login."
        )

        return redirect("login")

    return render(request, "accounts/register.html")  

@login_required
def manage_expenses(request):

    if request.method == "POST":
        if 'income_submit' in request.POST:
            amount = request.POST.get('income')
            Income.objects.create(user=request.user, amount=amount)
            messages.success(request, "Income added successfully!")

        else:
            title = request.POST.get('title')
            amount = request.POST.get('amount')
            category = request.POST.get('category')
            date = request.POST.get('date')

            Expense.objects.create(
                user=request.user,
                title=title,
                amount=amount,
                category=category,
                date=date
            )

            messages.success(request, "Expense added successfully!")

        return redirect('manage')

    # Fetch data
    expenses = Expense.objects.filter(user=request.user)

    # MONTHLY SUMMARY
    monthly_queryset = (
    expenses
    .annotate(month=TruncMonth("date"))
    .values("month")
    .annotate(total=Sum("amount"))
    .order_by("month")
)
    monthly_data = []
    
    for item in monthly_queryset:
        monthly_data.append({
                "month": item["month"].strftime("%b %Y"),
                "total": float(item["total"])
                })

    incomes = Income.objects.filter(user=request.user)

    total_income = incomes.aggregate(total=Sum("amount"))["total"] or 0

    total_expense = expenses.aggregate(total=Sum("amount"))["total"] or 0

    balance = total_income - total_expense

    transaction_count = expenses.count()

    category_queryset = (
    expenses
    .values("category")
    .annotate(total=Sum("amount"))
    .order_by("category")
    )
    
    category_data = []
    
    for item in category_queryset:
        category_data.append({
            "category": item["category"],
            "total": float(item["total"])
        })

    context = {
        "expenses": expenses,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "transaction_count": transaction_count,
        "monthly_data": monthly_data,
        "category_data": category_data,
    }

    return render(request, "dashboard/manage.html", context)

# edit expense

@login_required
def edit_expense(request, id):
    expense =  get_object_or_404(Expense, id=id, user=request.user)

    if request.method=="POST":
        expense.title = request.POST.get('title')
        expense.amount = request.POST.get('amount')
        expense.category = request.POST.get('category')
        expense.date = request.POST.get('date')

        expense.save()
        messages.info(request, "Expense updated successfully.")

        return redirect('manage')
    return render(request,'expenses/edit_expense.html', {'expense' : expense})

# Delete Expense

@login_required
def delete_expense(request, id):

    if request.method == "POST":
        expense = get_object_or_404(
            Expense,
            id=id,
            user=request.user
        )
        expense.delete()
        messages.error(request, "Expense deleted successfully.")

    return redirect("manage")
    
# Data_Visualization
@login_required
def data_visualization(request):

    expenses = Expense.objects.filter(user=request.user)

    #Filter Logic
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if category: expenses = expenses.filter(category=category)

    if start_date: expenses = expenses.filter(date__gte=start_date)

    if end_date: expenses = expenses.filter(date__lte=end_date)

    
    return render(request,'dashboard/visualization.html', context)

# LOGOUT FUNCTION
def logout_view(request):
    logout(request)
    return redirect('login')

