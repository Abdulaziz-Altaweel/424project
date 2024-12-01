from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Item
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Dynamically use the custom user model
        fields = ('username', 'email', 'password1', 'password2')



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']