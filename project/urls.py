from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('home.urls', namespace="home", )),
    url(r'^schools/', include('schools.urls', namespace="schools", )),
    url(r'^my_schools/', include('my_schools.urls', namespace="my_schools", )),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')), 
    url(r'^administration/', include(admin.site.urls)),

    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': "%s/home/fonts" % settings.STATIC_ROOT,
    }),
)
