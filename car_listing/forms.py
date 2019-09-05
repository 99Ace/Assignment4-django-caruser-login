from django import forms
from .models import Vehicle
from pyuploadcare.dj.forms import ImageField


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
            'image',
            'status',
        )
        
class EditEntry(forms.ModelForm):
    class Meta:
        model = Vehicle        
        fields = (
            'car_make',
            'car_model',
            'car_type',
            'year_of_make',
            'price',
            'mileage',
            'description',
            'image',
            'status'
        )
