from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from positions.fields import PositionField
from sorl.thumbnail.fields import ImageField


class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'))
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
        help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site)


    class Meta:
        db_table = 'django_flatpage'
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('title',)

    def __unicode__(self):
        return u"%s -- %s" % (self.title, self.url)

    def get_absolute_url(self):
        return self.url


class FlatPageImage(models.Model):
    page = models.ForeignKey(FlatPage, related_name='images')
    title = models.CharField(_("Title"), max_length=256, blank=True, null=True)
    image = ImageField(upload_to='images/flatpages', verbose_name=_("Image"))
    position = PositionField(collection='page')

    class Meta:
        verbose_name = _("flat page image")
        verbose_name_plural = _("flat page images")
        ordering = ('position',)

    def __unicode__(self):
        return 'image for %s' % unicode(self.page)