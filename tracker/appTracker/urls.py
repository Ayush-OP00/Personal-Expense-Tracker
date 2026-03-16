from django.urls import path  
from appTracker.views import registration

urlpatterns = [
    path('', registration, name = 'reg'),
]
