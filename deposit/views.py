import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

# Create your views here.
def place_deposit(request):

    amount = 200000 # prefix amount of $2,000 for deposit
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'place_deposit.html', {
        'key' : key,
        'amount' : amount
        })
    
    