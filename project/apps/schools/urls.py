from django.conf.urls.defaults import include, url
import dselector
parser = dselector.Parser()
url = parser.url

from schools import views

urlpatterns = parser.patterns('',
    url('{school_name:slug}/', views.detail, name='detail'),
)
