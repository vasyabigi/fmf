from django.conf.urls.defaults import patterns, url
from views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index-view'),
    url(r'^pages(?P<url>.*)$', 'django.contrib.flatpages.views.flatpage', name='flatpage_url'),
)
