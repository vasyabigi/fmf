from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from core.admin import BaseTranslationAdmin, BaseTranslationTabularInLine
from models import FlatPage, FlatPageImage

from tinymce.widgets import TinyMCE


class FlatPageImageInLine(BaseTranslationTabularInLine):
    model = FlatPageImage
    extra = 1


class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))

    class Meta:
        model = FlatPage


class FlatPageAdmin(BaseTranslationAdmin):
    form = FlatpageForm

    list_display = ('title', 'url')

    inlines = (FlatPageImageInLine,)

    fieldsets = (
        (None, {'fields': ('title', 'url', 'content',)}),
        (_("Meta information"), {'fields': ('meta_keywords', 'meta_description', 'meta_title')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('template_name', 'sites')}),
    )


    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name.startswith('content_'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 70, 'rows': 25, 'class':'vLargeTextField modeltranslation modeltranslation-default'},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(FlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(FlatPage, FlatPageAdmin)
