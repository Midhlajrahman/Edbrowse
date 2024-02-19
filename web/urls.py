from django.urls import path

from . import views

app_name = "web"


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("country/", views.country, name="country"),
    path("country-details/<str:slug>/", views.country_details, name="country_details"),
    path("courses/", views.courses, name="courses"),
    path("course-details/<str:slug>/", views.course_details, name="course_details"),
    path("services/", views.services, name="services"),
    path("service/<slug:slug>/", views.service_details, name="service_details"),
    path("alumini/", views.alumini, name="alumini"),
    path("alumini_details/<str:slug>/", views.alumini_details, name="alumini_details"),
    path("blog/", views.blog, name="blogs"),
    path("blog/<str:slug>/detail", views.blog_details, name="blog_details"),
    path("events/", views.event, name="events"),
    path("event/<str:slug>/detail/", views.event_details, name="event_details"),
    path("contact/", views.contact, name="contact"),
    path("testimonials/", views.testimonial, name="testimonial"),
    path("core-values/", views.core_values, name="core_values"),
]
