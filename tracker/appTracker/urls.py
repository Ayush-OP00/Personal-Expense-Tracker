from django.urls import path
from django.contrib.auth import views as auth_views
from appTracker.views import registration, login_view, manage_expenses, edit_expense, delete_expense, data_visualization, logout_view

urlpatterns = [
    path('', registration, name='reg'),
    # path('login/', login_view, name='login'), >> More secure line
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('manage/', manage_expenses, name='manage'),

    path('edit/<int:id>/', edit_expense, name='edit_expense'),

    path('delete/<int:id>/', delete_expense, name='delete_expense'),

    path('dashboard/', data_visualization, name='dashboard'),

    path('logout/', logout_view, name='logout'),
]