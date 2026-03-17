from django.urls import path
from appTracker.views import registration, login_view, manage_expenses, edit_expense, delete_expense, data_visualization, logout_view

urlpatterns = [
    path('', registration, name='reg'),
    path('login/', login_view, name='login'),

    path('manage/', manage_expenses, name='manage'),

    path('edit/<int:id>/', edit_expense, name='edit_expense'),

    path('delete/<int:id>/', delete_expense, name='delete_expense'),

    path('dashboard/', data_visualization, name='dashboard'),

    path('logout/', logout_view, name='logout'),
]