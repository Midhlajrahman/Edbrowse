from django.contrib import admin

from .models import (
    Alumini,
    Blog,
    Contact,
    Country,
    CountryFeature,
    Course,
    Enquiry,
    Event,
    EventEnquiry,
    Faq,
    Gallery,
    Service,
    ServiceEnquiry,
    SubCourse,
    Testimonial,
)

# Register your models here.


class CountryFeatureInline(admin.TabularInline):
    model = CountryFeature
    fields = (
        "feature_title",
        "feature_description",
        "feature_image",
    )
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_name",)
    prepopulated_fields = {"slug": ("country_name",)}
    inlines = [CountryFeatureInline]


class SubCourseInline(admin.TabularInline):
    model = SubCourse
    fields = ("sub_course",)
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)
    prepopulated_fields = {"slug": ("course_name",)}
    inlines = [SubCourseInline]


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


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name",)


@admin.register(ServiceEnquiry)
class ServiceEnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name",)


@admin.register(EventEnquiry)
class EventEnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("question",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Alumini)
class AluminiAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
