from django.shortcuts import render

# Create your views here.
def place_deposit(request):
    return render(request, 'place_deposit.html')
    