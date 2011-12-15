from django.conf.urls.defaults import patterns, url
from views import EventList, EventPastList, event_details

urlpatterns = patterns('',
    url(r'^$', EventList.as_view(), name='event-list'),
    url(r'^past/$', EventPastList.as_view(), name='event-list-past'),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', event_details, name='event-detail'),
)

