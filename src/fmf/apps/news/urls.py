from django.conf.urls.defaults import patterns, url
from views import NewsList, NewsDetails

urlpatterns = patterns('',
    url(r'^$', NewsList.as_view(), name='news-list'),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', NewsDetails.as_view(), name='news-detail'),
)
