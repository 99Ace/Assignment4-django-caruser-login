from django.shortcuts import render

# Create your views here.
def listing(request):
    return render(request, 'listing.html')
    
def add_listing(request):
    return render(request, 'add_listing.html')
    
def edit_listing(request):
    return render(request, 'edit_listing.html')

def delete_listing(request):
    return render(request, 'delete_listing.html')    