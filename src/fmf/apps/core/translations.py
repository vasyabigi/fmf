from modeltranslation.translator import translator, TranslationOptions
from news.models import News, NewsImage, Event
from django.contrib.flatpages.models import FlatPage
from chunks.models import Chunk
from models import IndexTab


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class ChunkTranslationOptions(TranslationOptions):
    fields = ('content',)

class IndexTabTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Chunk, ChunkTranslationOptions)
translator.register(IndexTab, IndexTabTranslationOptions)
translator.register(Event, EventTranslationOptions)
