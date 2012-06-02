from annoying.decorators import render_to
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@render_to("home/home.html")
def home(request):
    return locals()
