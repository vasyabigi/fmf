from django.db import models
from django.utils.translation import ugettext_lazy as _

from positions.fields import PositionField
from sorl.thumbnail.fields import ImageField


class Question(models.Model):
    question = models.TextField(_("question"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __unicode__(self):
        return self.question


class Feedback(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    image = ImageField(_("Image"), upload_to='images/feedback/', blank=True, null=True)
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'feedback-detail', (self.slug,)


class FeedbackQuestion(models.Model):
    feedback = models.ForeignKey(Feedback, verbose_name=_("Feedback"), related_name='questions')
    question = models.ForeignKey(Question, verbose_name=_("Question"))
    answer = models.TextField(_("Answer"))
    is_on_main = models.BooleanField(_("Can be main page?"), default=True)
    position = PositionField(collection='feedback')

    class Meta:
        verbose_name = _("Feedback question")
        verbose_name_plural = _("Feedback questions")
        unique_together = (('feedback', 'question'),)

    def __unicode__(self):
        return u'%s - %s' % (self.feedback, self.question)
