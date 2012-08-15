from annoying.decorators import render_to
from schools.models import School

@render_to("my_schools/home.html")
def home(request):
    school_slug = request.GET["s"]

    my_schools = [School.objects.get(slug__icontains=school_slug),]
    return locals()
