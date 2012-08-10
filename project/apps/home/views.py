from annoying.decorators import render_to
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@render_to("home/home.html")
def home(request):
    if request.POST:
        print request.POST

    return locals()


@render_to("home/upcoming_events.html")
def upcoming_events(request):
    return locals()
