from annoying.decorators import render_to
from schools.models import School
from my_schools.models import Person, PersonSchool


@render_to("my_schools/home.html")
def home(request):
    # school_slug = request.GET["s"]
    facebook = get_facebook_graph(request)
    print facebook.me()

    all_schools = School.objects.all()
    me = request.user.get_profile()

    my_schools = me.schools
    return locals()
