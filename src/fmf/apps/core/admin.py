from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline

from sorl.thumbnail.admin import AdminImageMixin


class BaseTranslationAdmin(AdminImageMixin, TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
            '/static/admin/js/editor.js',
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'all': ('/static/admin/css/editor.css',),
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }


class BaseTranslationTabularInLine(AdminImageMixin, TranslationTabularInline):
    pass

class BaseTranslationStackedInLine(AdminImageMixin, TranslationStackedInline):
    pass