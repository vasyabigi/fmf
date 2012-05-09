from modeltranslation.translator import translator, TranslationOptions
from chunks.models import Chunk
from news.models import News, NewsImage, Event
from flatpages_my.models import FlatPage, FlatPageImage
from feedbacks.models import Feedback
from seo.models import Seo
from sections.models import Section, Article, ArticleImage, SectionImage
from core.models import IndexSliderImage


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)


class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)


class ChunkTranslationOptions(TranslationOptions):
    fields = ('content',)


class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class FlatPageImageTranslationOptions(TranslationOptions):
    fields = ('title',)


class FeedbackTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class SeoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords')


class SectionTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


class SectionImageTranslationOptions(TranslationOptions):
    fields = ('title',)


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


class ArticleImageTranslationOptions(TranslationOptions):
    fields = ('title',)


class SeoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords')


class CoreImagesTranslationOptions(TranslationOptions):
    fields = ('custom_name',)


translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Chunk, ChunkTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(FlatPageImage, FlatPageImageTranslationOptions)
translator.register(Feedback, FeedbackTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(Article, ArticleTranslationOptions)
translator.register(Seo, SeoTranslationOptions)
translator.register(ArticleImage, ArticleImageTranslationOptions)
translator.register(SectionImage, SectionImageTranslationOptions)
translator.register(IndexSliderImage, CoreImagesTranslationOptions)
