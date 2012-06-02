from annoying.decorators import render_to

@render_to("home/home.html")
def home(request):
    return locals()
