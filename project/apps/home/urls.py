from django.conf.urls.defaults import patterns, include, url

from home import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'upcoming-events', views.upcoming_events, name='upcoming_events'),
)
