from django.db import models
from django.template.base import Template
from django.template.context import Context
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from sections.models import Article, Section

from positions.fields import PositionField
from sorl.thumbnail.fields import ImageField
from sorl.thumbnail.helpers import ThumbnailError
from sorl.thumbnail.shortcuts import get_thumbnail


class IndexSliderImage(models.Model):

    page = models.OneToOneField(Article, verbose_name=_("Page"),
        unique=True, blank=True, null=True)
    section = models.OneToOneField(Section, verbose_name=_("Section"),
        unique=True, blank=True, null=True)
    image = ImageField(_("Image"), upload_to='images/index/')
    position = PositionField()
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        ordering = ('position',)
        verbose_name = _("Image for slider")
        verbose_name_plural = _("Images for slider")

    def __unicode__(self):
        return _('Image for %s') % self.get_page_title

    def get_page_url(self):
        if self.section:
            return self.section.get_absolute_url()
        elif self.page:
            return self.page.get_absolute_url()

    @property
    def get_page_title(self):
        if self.section:
            return self.section.title
        elif self.page:
            return self.page.title

    def thumb(self):
        try:
            im = get_thumbnail(self.image, '50x50', crop='center')
            t = Template('<img src="{{ image.url }}" alt="{{ alt }}" />')
            c = Context({"image": im, 'alt': self.page, })
            thum = t.render(c)
        except ThumbnailError:
            thum = _('No image')
        return  thum
    thumb.short_description = _('Image')
    thumb.allow_tags = True


def fill_empty_languages(instance, fields):
    empty_langs = dict()
    for field in fields:
        empty_langs[field] = list()
        for lang in settings.LANGUAGES:
            if not getattr(instance, '%s_%s' % (field, lang[0])):
                empty_langs[field].append(lang[0])
    #TODO make message in all languages
    text = "Content not avalible in this language."
    for field in fields:
        for lang in empty_langs[field]:
            setattr(instance, '%s_%s' % (field, lang), text)
