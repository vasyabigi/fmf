from django.conf.urls.defaults import patterns, url
from views import news_list, news_details

urlpatterns = patterns('',
    url(r'^$', news_list, name='news-list'),
    url(r'^(?P<slug>[a-z0-9_-]+)/$', news_details, name='news-detail'),
)
