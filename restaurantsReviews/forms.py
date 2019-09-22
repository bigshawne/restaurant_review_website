from django.forms import ModelForm, TextInput, URLInput, ClearableFileInput
from .models import Restaurant, Dish


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('user', 'date')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form_control'}),
            'phone': TextInput(attrs={'class': 'form_control'}),
            'url': URLInput(attrs={'class': 'form_coontrol'}),
        }

        labels = {
            'name': 'name',
            'address': 'address',
            'phone': 'phone',
            'url': 'website'
        }