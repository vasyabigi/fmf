from django.contrib import admin

from core.admin import BaseTranslationAdmin, BaseTranslationStackedInLine
from models import Section, Article, ArticleImage, SectionImage


class ArticleImageAdmin(BaseTranslationStackedInLine):
    model = ArticleImage
    extra = 0


class SectionImageAdmin(BaseTranslationStackedInLine):
    model = SectionImage
    extra = 0


class SectionAdmin(BaseTranslationAdmin):
    inlines = (SectionImageAdmin,)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Section, SectionAdmin)


class ArticleAdmin(BaseTranslationAdmin):
    list_display = ('__unicode__', 'position',)
    inlines = (ArticleImageAdmin,)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('section',)

admin.site.register(Article, ArticleAdmin)
