from django.contrib import admin

from core.admin import BaseTranslationAdmin, BaseTranslationTabularInLine
from models import Section, Article, ArticleImage


class ArticleImageAdmin(BaseTranslationTabularInLine):
    model = ArticleImage
    extra = 0


class SectionAdmin(BaseTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Section, SectionAdmin)


class ArticleAdmin(BaseTranslationAdmin):
    list_display = ('__unicode__', 'position',)
    inlines = (ArticleImageAdmin,)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('section',)

admin.site.register(Article, ArticleAdmin)
