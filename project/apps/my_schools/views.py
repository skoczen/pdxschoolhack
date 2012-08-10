from annoying.decorators import render_to
from schools.models import School

@render_to("my_schools/home.html")
def home(request):
    my_schools = [School.objects.get(name__icontains="eff"),]
    return locals()
