from django.contrib import admin

from core.admin import BaseTranslationAdmin, BaseTranslationTabularInLine
from models import Section, Article, ArticleImage
from imperavi.admin import ImperaviModelAdmin


class ArticleImageAdmin(BaseTranslationTabularInLine):
    model = ArticleImage


class SectionAdmin(ImperaviModelAdmin, BaseTranslationAdmin):
    pass

admin.site.register(Section, SectionAdmin)


class ArticleAdmin(ImperaviModelAdmin, BaseTranslationAdmin):
    inlines = (ArticleImageAdmin,)

admin.site.register(Article, ArticleAdmin)
