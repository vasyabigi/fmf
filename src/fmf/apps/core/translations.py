from modeltranslation.translator import translator, TranslationOptions

from chunks.models import Chunk
from news.models import News, NewsImage, Event
from flatpages_my.models import FlatPage, FlatPageImage


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'meta_keywords', 'meta_description')

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'meta_keywords', 'meta_description')

class ChunkTranslationOptions(TranslationOptions):
    fields = ('content',)

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'meta_keywords', 'meta_description')

class FlatPageImageTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Chunk, ChunkTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(FlatPageImage, FlatPageImageTranslationOptions)
