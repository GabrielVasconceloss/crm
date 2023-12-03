from django import forms
from .models import status


class StatusForm(forms.ModelForm):
    class Meta:
        model = status
        fields = ['title', 'description', 'title_color', 'text_color']