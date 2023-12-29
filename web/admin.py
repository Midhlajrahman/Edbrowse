from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_name",)
    prepopulated_fields = {"slug": ("country_name",)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)
    prepopulated_fields = {"slug": ("course_name",)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name",)
    prepopulated_fields = {"slug": ("service_name",)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name",)