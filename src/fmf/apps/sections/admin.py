from django.contrib import admin

from core.admin import BaseTranslationAdmin, BaseTranslationTabularInLine
from models import Section, Article, ArticleImage


class ArticleImageAdmin(BaseTranslationTabularInLine):
    model = ArticleImage


class SectionAdmin(BaseTranslationAdmin):
    pass

admin.site.register(Section, SectionAdmin)


class ArticleAdmin(BaseTranslationAdmin):
    inlines = (ArticleImageAdmin,)

admin.site.register(Article, ArticleAdmin)
