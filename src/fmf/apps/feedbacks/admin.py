from django.contrib import admin

from core.admin import BaseTranslationAdmin, BaseTranslationStackedInLine
from models import Question, Feedback, FeedbackQuestion


class QuestionAdmin(BaseTranslationAdmin):
    pass


class FeedbackQuestionInline(BaseTranslationStackedInLine):
    model = FeedbackQuestion
    extra = 1


class FeedbackAdmin(BaseTranslationAdmin):
    inlines = (FeedbackQuestionInline,)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
