from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
                'email': forms.EmailInput(attrs={'class': 'form-control required email', 'placeholder': 'Enter Email'}),
                'subject': forms.TextInput(attrs={'class': 'form-control required', 'placeholder': 'Enter Subject'}),
                'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
                'message': forms.Textarea(attrs={'class': 'form-control required', 'rows': 7, 'placeholder': 'Enter Message'}),
            }
