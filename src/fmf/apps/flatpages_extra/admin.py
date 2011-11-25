from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from core.admin import BaseTranslationAdmin


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
    list_display = ('url', 'title')
    search_fields = ('url', 'title')
    exclude = ('content',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name.startswith('content'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 70, 'rows': 25, 'class':'vLargeTextField modeltranslation modeltranslation-default'},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(FlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
