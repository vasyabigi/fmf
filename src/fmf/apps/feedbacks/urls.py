from django.conf.urls.defaults import patterns, url

from views import feedbacks_list, feedback_details

urlpatterns = patterns('',
    url(r'^$', feedbacks_list, name='feedback-list'),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', feedback_details, name='feedback-detail'),
)
