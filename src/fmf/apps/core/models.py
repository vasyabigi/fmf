from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import reverse
from django.db import models
from django.template.base import Template
from django.template.context import Context
from django.utils.translation import ugettext_lazy as _

from positions.fields import PositionField
from pytils.translit import slugify
from sorl.thumbnail.fields import ImageField
from sorl.thumbnail.helpers import ThumbnailError
from sorl.thumbnail.shortcuts import get_thumbnail


class IndexSliderImage(models.Model):
    page = models.OneToOneField(FlatPage, verbose_name=_("Page"), unique=True)
    image = ImageField(_("Image"), upload_to='index/images/')
    position = PositionField()
    is_active = models.BooleanField(_("Active"), default=True)


    class Meta:
        ordering = ('position',)
        verbose_name = _("Image for slider")
        verbose_name_plural = _("Images for slider")

    def __unicode__(self):
        return _('Image for %s') % self.page

    def get_url(self):
        return reverse('django.contrib.flatpages.views.flatpage', args=(self.page.url,))

    def thumb(self):
        try:
            im = get_thumbnail(self.image, '50x50', crop='center')
            t = Template('<img src="{{ image.url }}" alt="{{ alt }}" />')
            c = Context({"image": im, 'alt': self.page })
            thum = t.render(c)
        except ThumbnailError:
            thum = _('No image')
        return  thum
    thumb.short_description = _('Image')
    thumb.allow_tags = True
