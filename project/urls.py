from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

import dselector
parser = dselector.Parser()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = parser.patterns('',
    url(r'', include('home.urls'), name="home"),
    url(r'^schools/', include('schools.urls'), name="schools"),
    url(r'^my_schools/', include('my_schools.urls'), name="my_schools"),
    url(r'^administration/', include(admin.site.urls)),

    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': "%s/home/fonts" % settings.STATIC_ROOT,
    }),
)
