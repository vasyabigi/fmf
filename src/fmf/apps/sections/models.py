from django.db import models
from django.utils.translation import ugettext_lazy as _
from positions.fields import PositionField
from sorl.thumbnail.fields import ImageField


class Section(models.Model):
    title = models.CharField(_('Title'), max_length=256)
    slug = models.SlugField(_('Slug'))
    content = models.TextField(_('Content'), blank=True, null=True)
    position = PositionField(default=0)

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ('position',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'section-details', (self.slug,)


class SectionImage(models.Model):
    section = models.ForeignKey(Section, related_name='images', verbose_name=_("section"))
    title = models.CharField(_("Title"), max_length=256, blank=True, null=True)
    image = ImageField(upload_to='images/sections', verbose_name=_("Image"))
    position = PositionField(collection='section')

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ('position',)

    def __unicode__(self):
        return u'image for %s' % self.section.title


class Article(models.Model):
    section = models.ForeignKey(Section, verbose_name=_("Section"),
        related_name='articles', blank=True, null=True
    )
    title = models.CharField(_('Title'), max_length=256)
    slug = models.SlugField(_('Slug'))
    content = models.TextField(_('Content'), blank=True, null=True)
    additional_menu = models.TextField(_('Additional menu'), blank=True, null=True)
    position = PositionField(collection='section', default=0)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ('title_uk',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'article-details', (self.section.slug, self.slug)


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', verbose_name=_("Article"))
    title = models.CharField(_("Title"), max_length=256, blank=True, null=True)
    image = ImageField(upload_to='images/articles', verbose_name=_("Image"))
    position = PositionField(collection='article')

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ('position',)

    def __unicode__(self):
        return u'image for %s' % self.article.title
