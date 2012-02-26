from django.conf.urls.defaults import url, patterns
from imperavi.views import redactor_upload
from imperavi.forms import FileForm

urlpatterns = patterns('',
    url('^upload/image/(?P<upload_to>.*)', redactor_upload, {
        'response': lambda name, url: '<img src="%s" title="%s">' % (url, name) ,
    }, name='redactor_upload_image'),
    url('^upload/file/(?P<upload_to>.*)', redactor_upload, {
        'form_class': FileForm,
        'response': lambda name, url: '<a href="%s">%s</a>' % (url, name),
    }, name='redactor_upload_file'),
)
