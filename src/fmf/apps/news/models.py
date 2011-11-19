from django.core.urlresolvers import reverse
from django.db import models
from django.template.base import Template
from django.template.context import Context
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField
from sorl.thumbnail.shortcuts import get_thumbnail
from positions import PositionField


class News(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField(_("Slug"), max_length=256)
    main_image = ImageField(upload_to='news/images', verbose_name=_("Main image"), blank=True, null=True)
    short_description = models.TextField(_("Short Description"))
    description = models.TextField(_("Description"))
    date = models.DateField(_("Date"), blank=True, null=True)
    is_main = models.BooleanField(_("Is on main page"), default=True)
    position = PositionField()
    is_active = models.BooleanField(_("Active"), default=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)

    class Meta:
        ordering = ('created',)
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", args=(self.slug,))

    def thumb(self):
        im = get_thumbnail(self.main_image, '50x50', crop='center')
        t = Template('<img src="{{ image.url }}" alt="{{ alt }}" />')
        c = Context({"image": im, 'alt': self.title })
        thum = t.render(c)
        return  thum
    thumb.short_description = _('Image')
    thumb.allow_tags = True


class NewsImage(models.Model):
    news = models.ForeignKey(News, verbose_name=_("News"), related_name='images')
    title = models.CharField(_("Title"), max_length=256, blank=True, null=True)
    image = ImageField(upload_to='news/images/', verbose_name=_("Image"))
    position = PositionField(collection='news')

    class Meta:
        ordering = ('title', 'news')
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __unicode__(self):
        if self.title:
            return 'image for %s - %s' % (self.news.title, self.title)
        else:
            return 'image for %s' % self.news.title
