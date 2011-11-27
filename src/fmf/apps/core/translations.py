from modeltranslation.translator import translator, TranslationOptions
from news.models import News, NewsImage
from django.contrib.flatpages.models import FlatPage
from chunks.models import Chunk


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class ChunkTranslationOptions(TranslationOptions):
    fields = ('content',)
    

translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Chunk, ChunkTranslationOptions)