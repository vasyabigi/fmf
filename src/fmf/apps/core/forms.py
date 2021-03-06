from django import forms
from flatpages_my.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class FlatpageForm(forms.ModelForm):

    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))

    class Meta:
        model = FlatPage


class ContactForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'name':'email',
        'class':'validate[required,custom[email]]',
        'placeholder': _("Email"),
    }))
    name = forms.CharField(max_length=256, label="", widget=forms.TextInput(attrs={
        'class':'validate[required]',
        'placeholder': _("Name"),
    }))
    content = forms.CharField(max_length=2048, label="", widget=forms.Textarea(attrs={
        'class':'validate[required]',
        'placeholder': _("Message"),
    }))


class QuestionForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect, choices=((1,1), (2,2), (3,3)))