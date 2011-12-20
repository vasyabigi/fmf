from django.conf.urls.defaults import patterns, url
from views import IndexView
from news.feeds import LatestNewsFeed, LatestEventsFeed

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index-view'),
    url(r'^rss/news/', LatestNewsFeed()),
    url(r'^rss/events/', LatestEventsFeed()),
)
