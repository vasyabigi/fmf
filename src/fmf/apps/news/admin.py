from django.contrib import admin

from core.admin import BaseTranslationAdmin, BaseTranslationTabularInLine
from models import News, NewsImage


class NewsImageAdmin(BaseTranslationTabularInLine):
    model = NewsImage
    extra = 1


class NewsAdmin(BaseTranslationAdmin):
    list_display = ('title', 'thumb', 'short_description', 'position')
    list_display_links = ('title', 'thumb')
    prepopulated_fields = {'slug': ('title',)}


class EventAdmin(BaseTranslationAdmin):
    list_display = ('title', 'date_from', 'date_to', 'short_description',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, NewsAdmin)
# admin.site.register(Event, EventAdmin)
