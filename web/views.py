import json
import urllib.parse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from web.forms import ContactForm, CourseEnquiryForm, EventEnquiryForm, ServiceEnquiryForm,CountryForm
from web.models import (
    Alumini,
    Blog,
    Country,
    CountryFeature,
    Course,
    Event,
    Faq,
    Service,
    Testimonial,
)

from .models import SubCourse

# Create your views here.


def index(request):
    services = Service.objects.all()
    courses = Course.objects.all()
    blogs = Blog.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    countries = Country.objects.all()[:4]

    if request.method == "POST":
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact You Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": form.errors.as_json(),
            }
        return JsonResponse(response_data)
    else:
        form = ContactForm()

    context = {
        "services": services,
        "courses": courses,
        "blogs": blogs,
        "form": form,
        "testimonials": testimonials,
        "faqs": faqs,
        "countries": countries,
    }
    return render(request, "web/index.html", context)


def about(request):
    faqs = Faq.objects.all()
    context = {"faqs": faqs}
    return render(request, "web/about.html", context)


def country(request):
    countries = Country.objects.all()

    context = {"countries": countries}
    return render(request, "web/country.html", context)


def country_details(request, slug):
    country_detail = Country.objects.get(slug=slug)
    testimonials = Testimonial.objects.all()
    country = get_object_or_404(Country, slug=slug)
    country_feature = CountryFeature.objects.filter(country=country)

    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.country_name = country
            data.save()

            # Send an email with the form data
            subject = "Country Enquiry Information"
            message = (
                f'Enquiry For: {data.country_name} \n'
                f'Name: {form.cleaned_data["name"]} \n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Subject: {form.cleaned_data["subject"]}\n'
                f'Phone: {form.cleaned_data["phone"]}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )

            from_email = "midlajrahman016@gmail.com"
            recipient_list = ["midlajrahman016@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Build the WhatsApp message
            whatsapp_message = (
                f'Enquiry For: {data.country_name} \n'
                f'Name: {form.cleaned_data["name"]} \n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Subject: {form.cleaned_data["subject"]}\n'
                f'Phone: {form.cleaned_data["phone"]}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+917736603496"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            # Redirect to the WhatsApp link
            return redirect(whatsapp_url)

        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")

            return JsonResponse({"status": "false", "title": "Form Validation Error", "message": form.errors})

    else:
        form = CountryForm()

    context = {
        "country_detail": country_detail,
        "form": form,
        "testimonials": testimonials,
        "country_feature": country_feature,
    }
    return render(request, "web/country-details.html", context)


def courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "web/courses.html", context)


def course_details(request, slug):
    course_detail = Course.objects.get(slug=slug)
    course = get_object_or_404(Course, slug=slug)
    sub_course = SubCourse.objects.filter(course=course)

    if request.method == "POST":
        form = CourseEnquiryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.course_name = course
            data.save()

            # Send an email with the form data
            subject = "Course Enquiry Information"
            message = (
                f'Enquiry For: {data.course_name}  \n'
                f'Name: {form.cleaned_data["full_name"]}  \n'
                f'Email: {form.cleaned_data["email"]} \n'
                f'Phone: {form.cleaned_data["phone"]} \n'
                f'current_education: {form.cleaned_data["current_education"]} \n'
                f'intended_study_abroad: {form.cleaned_data["intended_study_abroad"]} \n'
                f'area_of_study_interest: {form.cleaned_data["area_of_study_interest"]} \n'
                f'preferred_country: {form.cleaned_data["preferred_country"]} \n'
                f'preferred_university_or_region: {form.cleaned_data["preferred_university_or_region"]} \n'
                f'intended_course_of_study: {form.cleaned_data["intended_course_of_study"]} \n'
                f'language_proficiency: {form.cleaned_data["language_proficiency"]} \n'
                f'standardized_tests_taken: {form.cleaned_data["standardized_tests_taken"]} \n'
                f'financial_consideration: {form.cleaned_data["financial_consideration"]} \n'
                f'message: {form.cleaned_data["message"]} \n'
                f'source: {form.cleaned_data["source"]} \n'
            )

            from_email = "midlajrahman016@gmail.com"
            recipient_list = ["midlajrahman016@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Build the WhatsApp message
            whatsapp_message = (
                f'Enquiry For: {data.course_name}  \n'
                f'Name: {form.cleaned_data["full_name"]}  \n'
                f'Email: {form.cleaned_data["email"]} \n'
                f'Phone: {form.cleaned_data["phone"]} \n'
                f'current_education: {form.cleaned_data["current_education"]} \n'
                f'intended_study_abroad: {form.cleaned_data["intended_study_abroad"]} \n'
                f'area_of_study_interest: {form.cleaned_data["area_of_study_interest"]} \n'
                f'preferred_country: {form.cleaned_data["preferred_country"]} \n'
                f'preferred_university_or_region: {form.cleaned_data["preferred_university_or_region"]} \n'
                f'intended_course_of_study: {form.cleaned_data["intended_course_of_study"]} \n'
                f'language_proficiency: {form.cleaned_data["language_proficiency"]} \n'
                f'standardized_tests_taken: {form.cleaned_data["standardized_tests_taken"]} \n'
                f'financial_consideration: {form.cleaned_data["financial_consideration"]} \n'
                f'message: {form.cleaned_data["message"]} \n'
                f'source: {form.cleaned_data["source"]} \n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+917736603496"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            # Redirect to the WhatsApp link
            return redirect(whatsapp_url)

        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")

            return JsonResponse({"status": "false", "title": "Form Validation Error", "message": form.errors})

    else:
        form = CourseEnquiryForm()
        context = {
            "course_detail": course_detail,
            "form": form,
            "sub_course": sub_course,
        }
    return render(request, "web/course-details.html", context)


def services(request):
    services = Service.objects.all()
    context = {"services": services}
    return render(request, "web/services.html", context)


def service_details(request, slug):
    service_detail = Service.objects.get(slug=slug)
 
    if request.method == "POST":
        form = ServiceEnquiryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.service_name = service_detail
            data.save()

            # Send an email with the form data
            subject = "Event Enquiry Information"
            message = (
                f'Enquiry For: {data.service_name}  \n'
                f'Name: {form.cleaned_data["full_name"]}  \n'
                f'Email: {form.cleaned_data["email"]} \n'
                f'Phone: {form.cleaned_data["phone"]} \n'
                f'Service: {data.service_name}\n'
                f'Message: {form.cleaned_data["message"]} \n'
            )

            from_email = "midlajrahman016@gmail.com"
            recipient_list = ["midlajrahman016@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Build the WhatsApp message
            whatsapp_message = (
                f'Enquiry For: {data.service_name}\n'
                f'Name: {form.cleaned_data["full_name"]}\n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Phone: {form.cleaned_data["phone"]}\n'
                f'Service: {data.service_name}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+917736603496"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            # Redirect to the WhatsApp link
            return redirect(whatsapp_url)

        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")

            return JsonResponse({"status": "false", "title": "Form Validation Error", "message": form.errors})

    else:
        form = ServiceEnquiryForm()
    context = {
        "service_detail": service_detail,
        "form": form,
    }
    return render(request, "web/service-details.html", context)


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "web/blog.html", context)


def blog_details(request, slug):
    blog_detail = Blog.objects.get(slug=slug)
    related_blogs = Blog.objects.exclude(slug=slug)[:4]
    context = {
        "blog_detail": blog_detail,
        "related_blogs": related_blogs,
    }
    return render(request, "web/blog-details.html", context)


def event(request):
    events = Event.objects.all()

    context = {"events": events}
    return render(request, "web/events.html", context)


def event_details(request, slug):
    event_detail = Event.objects.get(slug=slug)

    if request.method == "POST":
        form = EventEnquiryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.event = event_detail
            data.save()

            # Send an email with the form data
            subject = "Event Enquiry Information"
            message = (
                f'Enquiry For: {data.event} \n'
                f'Name: {form.cleaned_data["full_name"]} \n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Phone: {form.cleaned_data["phone"]}\n'
            )

            from_email = "midlajrahman016@gmail.com"
            recipient_list = ["midlajrahman016@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Build the WhatsApp message
            whatsapp_message = (
                f'Enquiry For: {data.event} \n'
                f'Name: {form.cleaned_data["full_name"]} \n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Phone: {form.cleaned_data["phone"]}\n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+917736603496"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            # Redirect to the WhatsApp link
            return redirect(whatsapp_url)

        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")

            return JsonResponse({"status": "false", "title": "Form Validation Error", "message": form.errors})

    else:
        form = EventEnquiryForm()
        context = {
        "event_detail": event_detail,
        "form": form,
        }
        return render(request, "web/event-details.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            # Send an email with the form data
            subject = "Contact Enquiry Information"
            message = (
                f'Name: {form.cleaned_data["name"]} \n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Phone: {form.cleaned_data["phone"]}\n'
                f'Subject: {form.cleaned_data["subject"]}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )

            from_email = "midlajrahman016@gmail.com"
            recipient_list = ["midlajrahman016@gmail.com"]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Build the WhatsApp message
            whatsapp_message = (
                f'Name: {form.cleaned_data["name"]} \n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Phone: {form.cleaned_data["phone"]}\n'
                f'Subject: {form.cleaned_data["subject"]}\n'
                f'Message: {form.cleaned_data["message"]}\n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+917736603496"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

            # Redirect to the WhatsApp link
            return redirect(whatsapp_url)

        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")

            return JsonResponse({"status": "false", "title": "Form Validation Error", "message": form.errors})

    else:
        form = ContactForm()
        context = {"form": form, "is_contact": True}
        return render(request, "web/contact.html", context)


def testimonial(request):
    testimonials = Testimonial.objects.all()

    context = {"testimonials": testimonials}
    return render(request, "web/testimonials.html", context)


def core_values(request):
    context = {}
    return render(request, "web/core-values.html", context)


def alumini(request):
    alumini = Alumini.objects.all()
    context = {"alumini": alumini}
    return render(request, "web/alumini.html", context)


def alumini_details(request, slug):
    alumini = get_object_or_404(Alumini, slug=slug)
    context = {
        "alumini": alumini,
    }
    return render(request, "web/alumini_details.html", context)
