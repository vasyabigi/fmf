from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.admin import BaseTranslationAdmin, BaseTranslationStackedInLine
from models import Question, Feedback, FeedbackQuestion


class QuestionAdmin(BaseTranslationAdmin):
    pass


class FeedbackQuestionInline(BaseTranslationStackedInLine):
    model = FeedbackQuestion
    extra = 1


class FeedbackAdmin(BaseTranslationAdmin):
    inlines = (FeedbackQuestionInline,)
    prepopulated_fields = {"slug":("name",)}


admin.site.register(Question, QuestionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
