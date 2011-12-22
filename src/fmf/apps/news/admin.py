from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from core.admin import BaseTranslationAdmin, BaseTranslationTabularInLine
from models import News, NewsImage, Event

from tinymce.widgets import TinyMCE


class NewsImageAdmin(BaseTranslationTabularInLine):
    model = NewsImage
    extra = 1


class NewsAdmin(BaseTranslationAdmin):
    list_display = ('title', 'thumb', 'short_description', 'position')
    list_display_links = ('title', 'thumb')
    inlines = (
        NewsImageAdmin,
    )
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name.startswith('description_'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 70, 'rows': 25, 'class':'vLargeTextField modeltranslation modeltranslation-default'},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class EventAdmin(BaseTranslationAdmin):
    list_display = ('title', 'date_from', 'date_to', 'short_description',)
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name.startswith('description_'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 70, 'rows': 25, 'class':'vLargeTextField modeltranslation modeltranslation-default'},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(EventAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
