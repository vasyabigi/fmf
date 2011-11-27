from chunks.models import Chunk
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.flatpages.models import FlatPage

from core.models import IndexSliderImage
from forms import FlatpageForm

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TranslationStackedInline
from sorl.thumbnail.admin import AdminImageMixin
from tinymce.widgets import TinyMCE



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
    list_display_links = ('thumb', 'page')

admin.site.register(IndexSliderImage, IndexSliderImageAdmin)


class FlatPageAdmin(BaseTranslationAdmin):
    form = FlatpageForm
    list_display = ('url', 'title')
    list_display_links = ('url', 'title')
    search_fields = ('url', 'title')
    exclude = ('content',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name.startswith('content'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 70, 'rows': 25, 'class':'vLargeTextField modeltranslation modeltranslation-default'},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(FlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


class ChunkAdmin(BaseTranslationAdmin):
    list_display = ('key',)
    search_fields = ('key', 'content')

admin.site.unregister(Chunk)
admin.site.register(Chunk, ChunkAdmin)