from annoying.decorators import render_to


@render_to("home/home.html")
def home(request):
    return locals()


@render_to("home/upcoming_events.html")
def upcoming_events(request):
    return locals()
