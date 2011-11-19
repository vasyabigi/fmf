from django.conf.urls.defaults import patterns, url
from views import CategoryDetail, story_detail

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-z0-9_-]+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^(?P<category_slug>[a-z0-9_-]+)/(?P<slug>[a-z0-9_-]+)/$', story_detail, name='story-detail'),
)
