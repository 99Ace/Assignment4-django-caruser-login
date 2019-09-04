from django.urls import path, include
from .views import place_deposit

urlpatterns = [
    path('place_deposit', place_deposit, name='place_deposit' ),
]