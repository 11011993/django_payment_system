from django.urls import path, include
from .views import coffee_payment

urlpatterns = [
    path('', coffee_payment, name='coffee-payment'),
]