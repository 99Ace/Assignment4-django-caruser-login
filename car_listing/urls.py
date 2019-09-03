from django.urls import path, include
from .views import listing, add_listing, edit_listing, delete_listing

urlpatterns = [
    path('', listing, name='listing'),
    path('add_listing/', add_listing, name='add_listing'),
    path('edit_listing/', edit_listing, name='edit_listing'),
    path('delete_listing/', delete_listing, name='delete_listing')
]