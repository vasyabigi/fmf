from django.contrib import admin

from core.admin import BaseTranslationAdmin, BaseTranslationTabularInLine
from models import News, NewsImage


class NewsImageAdmin(BaseTranslationTabularInLine):
    model = NewsImage
    extra = 1


class NewsAdmin(BaseTranslationAdmin):
    list_display = ('title', 'thumb', 'short_description')
    inlines = (
        NewsImageAdmin,
    )
    prepopulated_fields = {'slug':('title',)}

admin.site.register(News, NewsAdmin)