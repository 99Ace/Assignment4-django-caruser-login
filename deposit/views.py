import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from car_listing.models import Vehicle

# Create your views here.
def place_deposit(request,id):
    car = get_object_or_404(Vehicle, pk=id)
    
    amount = 200000 # prefix amount of $2,000 for deposit
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'place_deposit.html', {
        'key' : key,
        'amount' : amount,
        'd' : car
        })
    
