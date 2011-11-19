from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.fields import ImageField


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField(_("Slug"), max_length=256)
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        ordering = ('title',)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', args=(self.slug,))


class Story(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"), related_name='stories')
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField(_("Slug"), max_length=256)
    image = ImageField(upload_to='stories/images', verbose_name=_("Main image"), blank=True, null=True)
    description = models.TextField(_("Description"))
    is_active = models.BooleanField(_("Active"), default=True)
    #TODO add position

    class Meta:
        ordering = ('title',)
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story-detail', args=(self.category.slug, self.slug))
