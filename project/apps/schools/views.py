from annoying.decorators import render_to
from schools.models import School


@render_to("schools/detail.html")
def detail(request, school_name=None):
    school = School.objects.get(slug=school_name)
    return locals()
