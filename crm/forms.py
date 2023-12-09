from django import forms
from .models import status, Customer


class StatusForm(forms.ModelForm):
    class Meta:
        model = status
        fields = ['title', 'description', 'title_color', 'text_color']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']