from .models import Course
from .models import Service
from .models import Country


def main_context(request):
    services = Service.objects.all()
    countries = Country.objects.all()
    courses = Course.objects.all()
    return {"courses": courses, "countries": countries,"services": services, "domain": request.META["HTTP_HOST"]}