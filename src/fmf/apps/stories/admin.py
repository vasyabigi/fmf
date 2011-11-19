from django.contrib import admin
from core.admin import BaseTranslationAdmin
from models import Category, Story


class CategoryAdmin(BaseTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)


class StoryAdmin(BaseTranslationAdmin):
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Story, StoryAdmin)
