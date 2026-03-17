from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('food', 'food'),
        ('transport', 'transport'),
        ('shopping', 'shopping'),
        ('bills', 'bills'),
        ('other', 'other'),
    ]

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Income: {self.amount}"
