from django.contrib import admin

from core.admin import BaseTranslationAdmin
from models import Feedback


class FeedbackAdmin(BaseTranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Feedback, FeedbackAdmin)
