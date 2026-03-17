from django.urls import path
from appTracker.views import registration, login_view, manage_expenses, edit_expense, delete_expense

urlpatterns = [
    path('', registration, name='reg'),
    path('login/', login_view, name='login'),

    path('manage/', manage_expenses, name='manage'),

    path('edit/<int:id>/', edit_expense, name='edit_expense'),

    path('delete/<int:id>/', delete_expense, name='delete_expense'),
]