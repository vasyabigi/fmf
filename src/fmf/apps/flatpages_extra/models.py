from django.db import models
from django.utils.translation import ugettext_lazy as _
from flatpages_my.models import FlatPage
from positions.fields import PositionField
from sorl.thumbnail.fields import ImageField


class ExtraFlatPage(models.Model):
    page = models.ForeignKey(FlatPage, verbose_name=_("Flatpage"), unique=True)

    class Meta:
        verbose_name = _("Extra flat page")
        verbose_name_plural = _("Extra flat pages")

    def __unicode__(self):
        return self.page.title

    def text_url(self):
        return self.page.url[1:]


class ExtraFlatPageImage(models.Model):
    page = models.ForeignKey(ExtraFlatPage, related_name='images')
    title = models.CharField(_("Title"), max_length=256, blank=True, null=True)
    image = ImageField(upload_to='images/flatpages')
    position = PositionField(collection='page')

    class Meta:
        verbose_name = _("Extra flat page image")
        verbose_name_plural = _("Extra flat page images")
        ordering = ('position',)

    def __unicode__(self):
        return 'image for %s' % unicode(self.page.page)
