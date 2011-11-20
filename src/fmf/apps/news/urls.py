from django.conf.urls.defaults import patterns, url
from views import NewsList, news_details

urlpatterns = patterns('',
    url(r'^$', NewsList.as_view(), name='news-list'),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', news_details, name='news-detail'),
)
