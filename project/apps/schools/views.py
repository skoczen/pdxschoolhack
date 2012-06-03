from annoying.decorators import render_to


@render_to("schools/detail.html")
def detail(request, school_name_slug=None):
    return locals()
