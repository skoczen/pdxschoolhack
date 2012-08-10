from django.conf.urls.defaults import patterns, include, url

from my_schools import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)
