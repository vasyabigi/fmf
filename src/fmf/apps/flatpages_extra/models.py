from django.db import models
from django.template.base import Template
from django.template.context import Context
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage
from positions.fields import PositionField
from sorl.thumbnail.fields import ImageField
from sorl.thumbnail.helpers import ThumbnailError
from sorl.thumbnail.shortcuts import get_thumbnail


class ExtraFlatPage(models.Model):
    page = models.ForeignKey(FlatPage, verbose_name=_("Flatpage"))

    class Meta:
        verbose_name = _("Extra flat page")
        verbose_name_plural = _("Extra flat pages")

    def __unicode__(self):
        return self.page.title

    def text_url(self):
        return self.page.url[1:]


class ExtraFlatPageImage(models.Model):
    page = models.ForeignKey(ExtraFlatPage, related_name='images')
    image = ImageField(upload_to='images/flatpages')
    position = PositionField(collection='page')
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Extra flat page image")
        verbose_name_plural = _("Extra flat page images")
        ordering = ('position',)

    def __unicode__(self):
        return 'image for %s' % unicode(self.page.page)
