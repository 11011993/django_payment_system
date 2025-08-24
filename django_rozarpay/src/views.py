from django.shortcuts import render
from .forms import CoffeePaymentForm
import razorpay

# Create your views here.
def coffee_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU','gMxfhwgZ73ANYJQCeb1LMy7W'))
        response_payment = client.order.create(dict(amount=amount,currency = 'INR'))
        print(response_payment)
        form = CoffeePaymentForm('request.POST') or None
        return render(request, 'coffee_payment.html',{'form':form})
    form = CoffeePaymentForm()
    return render(request, 'coefee_payment.html',{'form':form})