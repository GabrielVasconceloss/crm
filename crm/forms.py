from django import forms
from .models import Status, Customer, Opportunity


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['title', 'description', 'title_color', 'text_color']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']


class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['opportunity_name', 'opportunity_description', 'amount', 'status']