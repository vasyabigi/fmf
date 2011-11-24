import uuid
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField
from positions import PositionField


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField(_("Slug"), max_length=256)
    position = PositionField(_("Position"))
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        ordering = ('position',)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', args=(self.slug,))

    @property
    def active_stories(self):
        return self.stories.filter(is_active=True)


class Story(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"), related_name='stories')
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField(_("Slug"), max_length=256)
    image = ImageField(upload_to='stories/images', verbose_name=_("Main image"), blank=True, null=True)
    description = models.TextField(_("Description"))
    position = PositionField(_("Position"),collection='category')
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        ordering = ('position',)
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story-detail', args=(self.category.slug, self.slug))


@receiver(pre_save, sender=Story)
def story_slug(sender, instance, **kwargs):
    if Story.objects.exclude(pk=instance.pk).filter(slug=instance.slug):
        instance.slug += unicode(uuid.uuid4())[:5]
