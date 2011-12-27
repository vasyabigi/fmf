from django.conf.urls.defaults import *

urlpatterns = patterns('flatpages_my.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
