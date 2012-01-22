# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver


class Seo(models.Model):
    title = models.CharField(_('Title'), max_length=255, blank=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    keywords = models.TextField(_('Keywords'), blank=True, null=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    class Meta:
        verbose_name = _('SEO fields')
        verbose_name_plural = _('SEO fields')
        unique_together = (("content_type", "object_id"),)

    def __unicode__(self):
        return self.title


class Url(models.Model):
    url = models.CharField(_('URL'), max_length=200, unique=True,
        help_text=_("This should be an absolute path, excluding the domain name. Example: '/events/search/'."))

    class Meta:
        verbose_name = _('URL')
        verbose_name_plural = _('URLs')

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
            return self.url

#Check slashes at the begin and end of url
@receiver(pre_save, sender=Url)
def check_url(sender, instance, **kwargs):
    url = instance.url
    if url[0] != u'/':
        url = '/%s' % url
    if url[-1] != u'/':
        url = '%s/' % url
    if instance.url != url:
        instance.url = url
