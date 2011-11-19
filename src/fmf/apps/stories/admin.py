from django.contrib import admin
from core.admin import BaseTranslationAdmin, BaseTranslationStackedInLine
from models import Category, Story


class StoryStackedAdmin(BaseTranslationStackedInLine):
    model = Story
    extra = 0


class CategoryAdmin(BaseTranslationAdmin):
    inlines = [
        StoryStackedAdmin,
    ]

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)


class StoryAdmin(BaseTranslationAdmin):
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Story, StoryAdmin)
