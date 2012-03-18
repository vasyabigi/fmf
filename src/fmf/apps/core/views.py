# -*- coding: utf-8 -*-
import datetime
import logging
from django.core.mail import mail_managers
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.utils import simplejson
from django.views.generic.base import TemplateView
from django.core.cache import cache

from models import IndexSliderImage
from forms import ContactForm
from news.models import News, Event
from feedbacks.models import Feedback
from sections.models import Section


logger = logging.getLogger("fmf.%s" % __name__)


class IndexView(TemplateView):
    template_name = 'core/index_view.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        images = cache.get('images', None)
        if not images:
            images = IndexSliderImage.objects.filter(is_active=True).select_related()
            cache.set('images', images)

        feedbacks = Feedback.objects.order_by('?').select_related()[:3]
        sections = Section.objects.all()
        context.update({
            'images': images,
            'news_list': News.objects.filter(is_active=True).select_related()[:3],
            'events': Event.objects.filter(is_active=True, date_to__gte=datetime.datetime.today()).order_by('-date_to')[:3],
            'feedbacks': feedbacks,
            'sections': sections,
        })
        return context


class Test404(TemplateView):
    template_name = '404.html'


class Test500(TemplateView):
    template_name = '500.html'


def contacts(request):
    form = ContactForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            #Mail managers
            subject = "Contact: %s (%s)" % (form.cleaned_data['name'], form.cleaned_data['email'])
            message = form.cleaned_data['content']
            html_message = render_to_string('contacts/manager_message.html', form.cleaned_data)
            mail_managers(subject, message, html_message=html_message)

            #TODO Mail person

            #Log to file
            logger.info('%s %s' % (subject, message))

            if request.is_ajax():
                response = render_to_string('contacts/ajax_response.html')
                response_dict = dict(content=response)
                return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
            return redirect('contact-thank-you')
    return TemplateResponse(request, 'contacts/contacts.html', context)


def contanct_thank_you(request):
    return TemplateResponse(request, 'contacts/thank_you.html')
