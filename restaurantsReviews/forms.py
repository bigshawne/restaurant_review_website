from django.forms import ModelForm, TextInput, URLInput, ClearableFileInput
from .models import Restaurant, Dish


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('user', 'date',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form_control'}),
            'phone': TextInput(attrs={'class': 'form_control'}),
            'url': URLInput(attrs={'class': 'form_control'}),
        }

        labels = {
            'name': 'Name',
            'address': 'Address',
            'phone': 'Phone',
            'url': 'Website'
        }


class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('user', 'date', 'restaurant',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'image': ClearableFileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Dishes',
            'description': 'Description',
            'price': 'Price',
            'image': 'Image',
        }
