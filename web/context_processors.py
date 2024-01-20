from .models import Country, Course, Service


def main_context(request):
    services = Service.objects.all()
    nav_countries = Country.objects.all()
    courses = Course.objects.all()
    return {
        "courses": courses,
        "nav_countries": nav_countries,
        "services": services,
        "domain": request.META["HTTP_HOST"],
    }
