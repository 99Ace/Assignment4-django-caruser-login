from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .forms import NewEntry, EditEntry
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
    
def edit_listing(request, id):
    item = get_object_or_404(Vehicle, pk=id)
    
    if request.method == "POST":
        edit_entry_form = EditEntry(request.POST, request.FILES, instance=item)
        if edit_entry_form.is_valid():
            edit_entry_form.carplate = item.carplate
            edit_entry_form.date = item.date
            edit_entry_form.save()
            return redirect(listing)
    else:
        edit_entry_form = EditEntry(instance=item)
        return render(request, 'edit_listing.html',{
            'form': edit_entry_form
        })


    return render(request, 'edit_listing.html')

def delete_listing(request):
    return render(request, 'delete_listing.html')    