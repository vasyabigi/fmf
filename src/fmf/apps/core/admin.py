from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline

from sorl.thumbnail.admin import AdminImageMixin

from core.models import IndexSliderImage


class BaseTranslationAdmin(AdminImageMixin, TranslationAdmin):
    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }


class BaseTranslationTabularInLine(AdminImageMixin, TranslationTabularInline):
    pass

class BaseTranslationStackedInLine(AdminImageMixin, TranslationStackedInline):
    pass

class IndexSliderImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('thumb', 'page', 'position')

admin.site.register(IndexSliderImage, IndexSliderImageAdmin)
