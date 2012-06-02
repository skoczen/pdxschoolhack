from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('home.urls'), name="home"),

    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': "%s/home/fonts" % settings.STATIC_ROOT,
    }),
)
