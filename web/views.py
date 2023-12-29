import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from web.forms import ContactForm, EnquiryForm, EventEnquiryForm, ServiceEnquiryForm

from web.models import Blog, Country, Course, Event, Service, ServiceEnquiry, Testimonial

# Create your views here.

def index(request):
    services = Service.objects.all()
    courses = Course.objects.all()
    blogs = Blog.objects.all()
    testimonials = Testimonial.objects.all()

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



    context ={
        "services":services,
        "courses":courses,
        "blogs":blogs,
        "form":form,
        "testimonials":testimonials
    }
    return render(request, 'web/index.html',context)

def about(request):
    
    context ={
    }
    return render(request, 'web/about.html',context)

def country(request):
    countries = Country.objects.all()

    context ={
        'countries':countries
    }
    return render(request, 'web/country.html',context)

def country_details(request,slug):
    country_detail = Country.objects.get(slug=slug)

    context ={
        'country_detail':country_detail
    }
    return render(request, 'web/country-details.html',context)



def courses(request):
    courses = Course.objects.all()
    context ={
        "courses":courses
    }
    return render(request, 'web/courses.html',context)

def course_details(request,slug):
    course_detail = Course.objects.get(slug=slug)    

    if request.method == "POST":
        form = EnquiryForm(request.POST or None, request.FILES or None)
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
        form = EnquiryForm()
    context ={
        "course_detail":course_detail,
        "form":form
    }
    return render(request, 'web/course-details.html',context)


def services(request):
    services = Service.objects.all()
    context ={
        "services":services
    }
    return render(request, 'web/services.html',context)


def service_details(request,slug):
    service_detail= Service.objects.get(slug=slug)

    form = ServiceEnquiryForm(
        service=service_detail.service_name, data=request.POST or None, files=request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
           
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact you Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "form2 validation error",
                "message": repr(form.errors),
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )

    

    context ={
            "service_detail":service_detail,
            "form":form,
        }
    return render(request, 'web/service-details.html',context)




def blog(request):
    blogs = Blog.objects.all()
    context ={
        "blogs":blogs
    }
    return render(request, 'web/blog.html',context)

def blog_details(request,slug):
    blog_detail = Blog.objects.get(slug=slug)
    related_blogs = Blog.objects.exclude(slug=slug)[:4]
    context ={
        "blog_detail":blog_detail,
        "related_blogs":related_blogs,
    }
    return render(request, 'web/blog-details.html',context)


def event(request):
    events = Event.objects.all()

    context ={
        "events":events
    }
    return render(request, 'web/events.html',context)

def event_details(request,slug):
    event_detail = Event.objects.get(slug=slug)

    form = EventEnquiryForm(
        event=event_detail.title, data=request.POST or None, files=request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
           
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact you Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "form2 validation error",
                "message": repr(form.errors),
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )

    context ={
        "event_detail":event_detail,
        "form":form,
    }
    return render(request, 'web/event-details.html',context)

def contact(request):
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
        context = {"form": form, "is_contact": True}
        return render(request, 'web/contact.html', context)