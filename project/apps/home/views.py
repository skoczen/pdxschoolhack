from annoying.decorators import render_to
from django.views.decorators.csrf import csrf_exempt

from schools.models import School


@csrf_exempt
@render_to("home/coming-soon.html")
def home(request):
    # all_schools = School.objects.all()
    return locals()


@render_to("home/upcoming_events.html")
def upcoming_events(request):
    return locals()
