from django import forms

from .models import Contact, CourseEnquiry, EventEnquiry, ServiceEnquiry, CountryEnquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Enter Email",
                }
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control required", "placeholder": "Enter Subject"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Enter Message",
                }
            ),
        }


class CountryForm(forms.ModelForm):
    class Meta:
        model = CountryEnquiry
        exclude = ("country_name",)

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Enter Email",
                }
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control required", "placeholder": "Enter Subject"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Phone"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Enter Message",
                }
            ),
        }

class CourseEnquiryForm(forms.ModelForm):
    class Meta:
        model = CourseEnquiry
        exclude = ("course_name",)

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Full Name",
                    "required": "true",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Email",
                    "required": "true",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Phone",
                    "required": "true",
                }
            ),
            "current_education": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Current Level of Education",
                    "required": "true",
                }
            ),
            "intended_study_abroad": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Intended Level of Study Abroad",
                    "required": "true",
                }
            ),
            "area_of_study_interest": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Area of Study Interest",
                    "required": "true",
                }
            ),
            "preferred_country": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Preferred Country",
                    "required": "true",
                }
            ),
            "preferred_university_or_region": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Preferred University or Region",
                    "required": "true",
                }
            ),
            "intended_course_of_study": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Intended Course of Study",
                    "required": "true",
                }
            ),
            "language_proficiency": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Language Proficiency",
                    "required": "true",
                }
            ),
            "standardized_tests_taken": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Have you taken any standardized tests (IELTS, TOEFL, etc.)?",
                    "required": "true",
                }
            ),
            "financial_consideration": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Financial Considerations",
                    "required": "true",
                }
            ),
            "message": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Message",
                    "required": "true",
                }
            ),
            "source": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Source",
                    "required": "true",
                }
            ),
        }


class ServiceEnquiryForm(forms.ModelForm):
    class Meta:
        model = ServiceEnquiry
        exclude = ("service",)
        

        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control required email", "placeholder": "Email"}
            ),
            "phone": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
           "message": forms.Textarea(
                attrs={
                    "class": "form-control required",
                    "rows": 5,
                    "placeholder": "Enter Message",
                }
            ),
        }


class EventEnquiryForm(forms.ModelForm):
    class Meta:
        model = EventEnquiry
        exclude = ("event",)

        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control required email", "placeholder": "Email"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
            
        }
