from chunks.models import Chunk
from django.contrib import admin

from models import IndexSliderImage

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline
from sorl.thumbnail.admin import AdminImageMixin
from imperavi.admin import ImperaviAdmin


class BaseTranslationAdmin(AdminImageMixin, TranslationAdmin, ImperaviAdmin):

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }


class BaseTranslationTabularInLine(AdminImageMixin, TranslationTabularInline):
    pass


class BaseTranslationStackedInLine(AdminImageMixin, TranslationStackedInline):
    pass


class IndexSliderImageAdmin(BaseTranslationAdmin):
    list_display = ('thumb', '__unicode__', 'position')
    list_display_links = ('thumb', '__unicode__')

admin.site.register(IndexSliderImage, IndexSliderImageAdmin)


class ChunkAdmin(BaseTranslationAdmin):
    list_display = ('key',)
    search_fields = ('key', 'content')

admin.site.unregister(Chunk)
admin.site.register(Chunk, ChunkAdmin)
