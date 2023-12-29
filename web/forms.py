from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput

from .models import Contact, Enquiry, EventEnquiry, ServiceEnquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
                'email': forms.EmailInput(attrs={'class': 'form-control required email', 'placeholder': 'Enter Email'}),
                'subject': forms.TextInput(attrs={'class': 'form-control required', 'placeholder': 'Enter Subject'}),
                'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
                'message': forms.Textarea(attrs={'class': 'form-control required', 'rows': 5, 'placeholder': 'Enter Message'}),
            }

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        exclude = ()

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control required email', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),

            'current_education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Level of Education'}),
            'intended_study_abroad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Intended Level of Study Abroad'}),
            'area_of_study_interest': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area of Study Interest'}),

            'preferred_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preferred Country'}),
            'preferred_university_or_region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preferred University or Region'}),
            'intended_course_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Intended Course of Study'}),

            'language_proficiency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Language Proficiency'}),
            'standardized_tests_taken': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Have you taken any standardized tests (IELTS, TOEFL, etc.)?'}),
            'financial_consideration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Financial Considerations'}),

            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),
            'source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source'}),
        }

class ServiceEnquiryForm(forms.ModelForm):
    class Meta:
        model = ServiceEnquiry
        exclude = ()

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control required email', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'service': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service',"readonly": "readonly",}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

    def __init__(self, service, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].initial = service


class EventEnquiryForm(forms.ModelForm):
    class Meta:
        model = EventEnquiry
        exclude = ()

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control required email', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'event': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event',"readonly": "readonly",}),
            
        }

    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"].initial = event