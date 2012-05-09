from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField


class Feedback(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    image = ImageField(_("Image"), upload_to='images/feedbacks/', blank=True, null=True)
    short_description = models.TextField(_("Short description"))
    description = models.TextField(_("Description"))
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'feedback-detail', (self.slug,)
