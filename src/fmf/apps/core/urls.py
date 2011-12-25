from django.conf.urls.defaults import patterns, url
from views import IndexView, Test404, Test500
from news.feeds import LatestNewsFeed, LatestEventsFeed

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index-view'),
    url(r'^rss/news/', LatestNewsFeed()),
    url(r'^rss/events/', LatestEventsFeed()),

    url(r'^404/$', Test404.as_view(), name='404'),
    url(r'^500/$', Test500.as_view(), name='500'),
)
