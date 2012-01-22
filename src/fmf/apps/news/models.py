import uuid
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.template.base import Template
from django.template.context import Context
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField
from sorl.thumbnail.helpers import ThumbnailError
from sorl.thumbnail.shortcuts import get_thumbnail
from positions import PositionField

from core.models import fill_empty_languages


class News(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField(_("Slug"), max_length=256)
    main_image = ImageField(upload_to='news/images', verbose_name=_("Main image"), blank=True, null=True)
    short_description = models.TextField(_("Short Description"))
    description = models.TextField(_("Description"))
    date = models.DateField(_("Date"), blank=True, null=True)
    position = PositionField(_("Position"), default=0)
    is_active = models.BooleanField(_("Active"), default=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)

    class Meta:
        ordering = ('position',)
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", args=(self.slug,))

    def thumb(self):
        try:
            im = get_thumbnail(self.main_image, '50x50', crop='center')
            t = Template('<img src="{{ image.url }}" alt="{{ alt }}" />')
            c = Context({"image": im, 'alt': self.title })
            thum = t.render(c)
        except ThumbnailError:
            thum = _('No image')
        return  thum
    thumb.short_description = _('Image')
    thumb.allow_tags = True

@receiver(pre_save, sender=News)
def news_slug(sender, instance, **kwargs):
    if News.objects.exclude(pk=instance.pk).filter(slug=instance.slug):
        instance.slug += unicode(uuid.uuid4())[:5]

@receiver(pre_save, sender=News)
def news_empty_languages(sender, instance, **kwargs):
    fill_empty_languages(instance, ('description', 'short_description'))



class NewsImage(models.Model):
    news = models.ForeignKey(News, verbose_name=_("News"), related_name='images')
    title = models.CharField(_("Title"), max_length=256, blank=True, null=True)
    image = ImageField(upload_to='images/news/', verbose_name=_("Image"))
    position = PositionField(_("Position"), collection='news')

    class Meta:
        ordering = ('position',)
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __unicode__(self):
        if self.title:
            return _('image for %(news_title)s - %(title)s') % {'news_title':self.news.title, 'title':self.title}
        else:
            return _('image for %s') % self.news.title


class Event(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    slug = models.SlugField(_("Slug"), max_length=256)
    date_from = models.DateField(_("Date from"), help_text=_("If date only one - put it just here"))
    date_to = models.DateField(_("Date to"), blank=True, null=True)
    image = ImageField(upload_to='images/events/', verbose_name=_("Main image"), blank=True, null=True)
    short_description = models.TextField(_("Short Description"))
    description = models.TextField(_("Description"))
    is_active = models.BooleanField(_("Active"), default=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-date_to',)
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event-detail", args=(self.slug,))

    def thumb(self):
        try:
            im = get_thumbnail(self.image, '50x50', crop='center')
            t = Template('<img src="{{ image.url }}" alt="{{ alt }}" />')
            c = Context({"image": im, 'alt': self.title })
            thum = t.render(c)
        except ThumbnailError:
            thum = _('No image')
        return  thum
    thumb.short_description = _('Image')
    thumb.allow_tags = True

@receiver(pre_save, sender=Event)
def put_date_to(sender, instance, **kwargs):
    if not instance.date_to:
        instance.date_to = instance.date_from

@receiver(pre_save, sender=Event)
def events_empty_languages(sender, instance, **kwargs):
    fill_empty_languages(instance, ('description', 'short_description'))
