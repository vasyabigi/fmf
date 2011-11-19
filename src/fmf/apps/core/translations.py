from modeltranslation.translator import translator, TranslationOptions

from news.models import News, NewsImage
from stories.models import Category, Story


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

class StoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Story, StoryTranslationOptions)
