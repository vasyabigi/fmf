from django.contrib import admin

from core.admin import BaseTranslationAdmin
from models import Section, Article


class SectionAdmin(BaseTranslationAdmin):
    pass

admin.site.register(Section, SectionAdmin)


class ArticleAdmin(BaseTranslationAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
