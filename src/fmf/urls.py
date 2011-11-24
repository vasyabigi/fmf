from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^localeurl/', include('localeurl.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),

    url(r'^', include('core.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^category/', include('stories.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)$" % settings.STATIC_URL[1:], "static.serve", {
            "document_root": settings.STATIC_ROOT,
            'show_indexes': True,
        }),
        url(r"%s(?P<path>.*)$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
