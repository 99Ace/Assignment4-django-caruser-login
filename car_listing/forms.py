from django import forms
from .models import Vehicle

class NewEntry(forms.ModelForm):
    class Meta:
        model = Vehicle        
        fields = (
            'carplate',
            'car_make',
            'car_model',
            'car_type',
            'year_of_make',
            'price',
            'mileage',
            'description',
            'status'
        )
