from modeltranslation.translator import translator, TranslationOptions
from news.models import News, NewsImage, Event
from django.contrib.flatpages.models import FlatPage
from chunks.models import Chunk
from flatpages_extra.models import ExtraFlatPageImage

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'meta_keywords', 'meta_description')

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'meta_keywords', 'meta_description')

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class ChunkTranslationOptions(TranslationOptions):
    fields = ('content',)

class ExtraFlatPageImageTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Chunk, ChunkTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(ExtraFlatPageImage, ExtraFlatPageImageTranslationOptions)
