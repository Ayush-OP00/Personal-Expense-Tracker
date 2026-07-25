from django.urls import path
from django.contrib.auth import views as auth_views
from appTracker.views import registration, login_view, manage_expenses, edit_expense, delete_expense, data_visualization, logout_view
from . import views

urlpatterns = [

    # Authentication
    path('', registration, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Expense Management
    path('manage/', manage_expenses, name='manage'),
    path('edit/<int:id>/', edit_expense, name='edit_expense'),
    path('delete/<int:id>/', delete_expense, name='delete_expense'),

    # Analytics
    path('dashboard/', data_visualization, name='dashboard'),

]