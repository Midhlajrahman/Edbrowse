from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField
# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    tag_line = models.CharField(max_length=250, null=True, blank=True)
    country_image = VersatileImageField("Country Image",  upload_to="Country/",ppoi_field="ppoi")
    cover_image = VersatileImageField("Country Cover Image",  upload_to="Country/",ppoi_field="ppoi")
    ppoi = PPOIField(("Image PPOI"))
    content = HTMLField()

    class Meta:
        verbose_name_plural = ("Countries")
        
    def __str__(self):
        return str(self.country_name)
    

    def get_absolute_url(self):
        return reverse("web:country_details", kwargs={"slug": self.slug})
    

class Course(models.Model):
    course_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    course_image = VersatileImageField("Course Image",  upload_to="Course/",ppoi_field="ppoi")
    cover_image = VersatileImageField("Course Cover Image",  upload_to="Course/",ppoi_field="ppoi")
    ppoi = PPOIField(("Image PPOI"))
    content = HTMLField()

    class Meta:
        verbose_name_plural = ("Courses")
        
    def __str__(self):
        return str(self.course_name)
    
    def get_absolute_url(self):
        return reverse("web:course_details", kwargs={"slug": self.slug})

class Service(models.Model):
    service_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    service_image = VersatileImageField("Service Image",  upload_to="Service/",ppoi_field="ppoi")
    cover_image = VersatileImageField("Service Cover Image",  upload_to="Service/",ppoi_field="ppoi")
    ppoi = PPOIField(("Image PPOI"))
    sub_content = models.TextField(null=True, blank=True)
    content = HTMLField()

    class Meta:
        verbose_name_plural = ("Services")
        
    def __str__(self):
        return str(self.service_name)
    
    def get_absolute_url(self):
        return reverse("web:service_details", kwargs={"slug": self.slug})
    

class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    blog_image = VersatileImageField("Blog Image",  upload_to="Blog/",ppoi_field="ppoi")
    cover_image = VersatileImageField("Blog Cover Image",  upload_to="Blog/",ppoi_field="ppoi")
    date = models.DateField(null=True, blank=True)
    ppoi = PPOIField(("Image PPOI"))
    content = HTMLField()

    class Meta:
        verbose_name_plural = ("Blogs")
        
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("web:blog_details", kwargs={"slug": self.slug})
    

class Event(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    event_image = VersatileImageField("Event Image",  upload_to="Event/",ppoi_field="ppoi")
    cover_image = VersatileImageField("Event Cover Image",  upload_to="Event/",ppoi_field="ppoi")
    ppoi = PPOIField(("Image PPOI"))
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=250)
    content = HTMLField()

    class Meta:
        verbose_name_plural = ("Events")
        
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("web:event_details", kwargs={"slug": self.slug})
    

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    class Meta:
        verbose_name_plural = ("Contacts")
        
    def __str__(self):
        return str(self.name)
    
class Enquiry(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)

    current_education = models.CharField(max_length=50, blank=True, null=True)
    intended_study_abroad = models.CharField(max_length=50, blank=True, null=True)
    area_of_study_interest = models.CharField(max_length=100, blank=True, null=True)

    preferred_country = models.CharField(max_length=50, blank=True, null=True)
    preferred_university_or_region = models.CharField(max_length=100, blank=True, null=True)
    intended_course_of_study = models.CharField(max_length=100, blank=True, null=True)

    language_proficiency = models.CharField(max_length=100,  blank=True, null=True)
    standardized_tests_taken = models.CharField(max_length=100, blank=True, null=True)
    financial_consideration = models.CharField(max_length=100, blank=True, null=True)

    message = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = ("Enquiries")
        
    def __str__(self):
        return str(self.full_name)
    

class ServiceEnquiry(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    service = models.CharField(max_length=250)
    message = models.TextField()

    class Meta:
        verbose_name_plural = ("Service Enquiries")
        
    def __str__(self):
        return str(self.full_name)
    
class EventEnquiry(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    event = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = ("Event Enquiries")
        
    def __str__(self):
        return str(self.full_name)
    
class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    description = models.TextField()
    photo = VersatileImageField("Testimonial Image",  upload_to="testimonials/",ppoi_field="ppoi")
    ppoi = PPOIField(("Image PPOI"))

    class Meta:
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return str(self.name)
    
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name_plural = ("FAQ's")

    def __str__(self):
        return str(self.question)
    
class Gallery(models.Model):
    image = VersatileImageField("Gallery Image",  upload_to="gallery/",ppoi_field="ppoi")
    ppoi = PPOIField(("Image PPOI"))
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return str(self.title)