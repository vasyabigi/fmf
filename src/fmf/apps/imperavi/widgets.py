from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.conf import settings

try:
    import simplejson as json
except ImportError:
    from django.utils import simplejson as json

def extend(dict1, dict2):
    return dict(dict1, **dict2)

OPTIONS = getattr(settings, 'IMPERAVI_OPTIONS', {'focus': True})

class ImperaviEditor(widgets.Textarea):

    class Media:
        js = (
            'js/redactor/redactor.js',
        )
        css = {
            'all': ('js/redactor/css/redactor.css', ),
        }

    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to', '')
        self.options = dict(OPTIONS, **kwargs.pop('redactor_options', {}))

        kwargs['attrs'] = extend({
            'cols': 100,
            'rows': 30,
        }, kwargs.get('attrs', {}))

        super(ImperaviEditor, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        input_ = super(ImperaviEditor, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')

        options = json.dumps(extend({
            'image_upload': reverse('redactor_upload_image', kwargs={'upload_to': self.upload_to}),
            'file_upload': reverse('redactor_upload_file', kwargs={'upload_to': self.upload_to}),
            'lang': 'ua',
        }, self.options))

        return mark_safe(input_ + (
            '<script type="text/javascript">' +
            'django.jQuery(document).ready(function(){' +
            'django.jQuery("#%s").redactor(%s);' % (id_, options) +
            '});</script>'
        ))
