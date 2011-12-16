from django.contrib import admin

from core.admin import BaseTranslationTabularInLine
from models import ExtraFlatPage, ExtraFlatPageImage

from sorl.thumbnail.admin import AdminImageMixin


class ExtraFlatPageImageInLine(BaseTranslationTabularInLine):
    model = ExtraFlatPageImage
    extra = 1


class ExtraFlatPageAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = (
        ExtraFlatPageImageInLine,
    )
    list_display = ('page',)

admin.site.register(ExtraFlatPage, ExtraFlatPageAdmin)
