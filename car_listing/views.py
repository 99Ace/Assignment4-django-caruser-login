from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from .forms import NewEntry
from .models import Vehicle

# Create your views here.

def listing(request):
    results = Vehicle.objects.all()
    return render(request, 'listing.html', {
        'details':results
    })
   
   
""" TO CREATE A NEW VEHICLE LISTING """  
def add_listing(request):
    if request.method == "POST":
        new_entry_form = NewEntry(request.POST, request.FILES)
        if new_entry_form.is_valid():
            new_entry_form.save()
            return redirect(listing)
    else:
        new_entry_form = NewEntry()
        return render(request, 'add_listing.html',{
            'form' : new_entry_form
        })
    
def edit_listing(request):
    return render(request, 'edit_listing.html')

def delete_listing(request):
    return render(request, 'delete_listing.html')    