from modeltranslation.translator import translator, TranslationOptions

from news.models import News, NewsImage
from stories.models import Category, Story
from django.contrib.flatpages.models import FlatPage


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

class StoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Story, StoryTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
