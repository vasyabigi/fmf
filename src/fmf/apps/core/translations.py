from modeltranslation.translator import translator, TranslationOptions

from news.models import News, NewsImage

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
