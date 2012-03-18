from django.conf.urls.defaults import patterns, url
from views import section_details, article_details

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', section_details, name='section-details'),
    url(
        r'^(?P<section_slug>[\w-]+)/(?P<article_slug>[\w-]+)/$',
        article_details, name='article-details'
    ),
)
