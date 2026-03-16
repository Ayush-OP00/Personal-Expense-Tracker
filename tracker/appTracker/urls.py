from django.urls import path  
from appTracker.views import registration, login_view

urlpatterns = [
    path('', registration, name = 'reg'),
    path('login', login_view, name ='login'),
]
