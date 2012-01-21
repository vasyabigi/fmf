from modeltranslation.translator import translator, TranslationOptions
from chunks.models import Chunk
from news.models import News, NewsImage, Event
from flatpages_my.models import FlatPage, FlatPageImage
from feedbacks.models import Question, Feedback, FeedbackQuestion
from seo.models import Seo


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'meta_keywords', 'meta_description')

class NewsImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description', 'meta_keywords', 'meta_description')

class ChunkTranslationOptions(TranslationOptions):
    fields = ('content',)

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'meta_keywords', 'meta_description', 'meta_title')

class FlatPageImageTranslationOptions(TranslationOptions):
    fields = ('title',)

class QuestionTranslationOptions(TranslationOptions):
    fields = ('question',)

class FeedbackTranslationOptions(TranslationOptions):
    fields = ('name',)

class FeedbackQuestionTranslationOptions(TranslationOptions):
    fields = ('answer',)

class SeoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords')


translator.register(News, NewsTranslationOptions)
translator.register(NewsImage, NewsImageTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Chunk, ChunkTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(FlatPageImage, FlatPageImageTranslationOptions)
translator.register(Question, QuestionTranslationOptions)
translator.register(Feedback, FeedbackTranslationOptions)
translator.register(FeedbackQuestion, FeedbackQuestionTranslationOptions)
translator.register(Seo, SeoTranslationOptions)