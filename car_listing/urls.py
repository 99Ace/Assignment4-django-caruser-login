from django.urls import path, include
from .views import listing, add_listing, edit_listing, delete_listing, confirm_delete

urlpatterns = [
    path('', listing, name='listing'),
    path('add_listing/', add_listing, name='add_listing'),
    path('edit_listing/<id>', edit_listing, name='edit_listing'),
    path('delete_listing/<id>', delete_listing, name='delete_listing'),
    path('confirm_delete/<id>', confirm_delete, name='confirm_delete' ),
]