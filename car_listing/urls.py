
from django.urls import path, include
from .views import listing
urlpatterns = [
    path('', listing, name='listing')
]