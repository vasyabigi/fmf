import datetime
from django.http import Http404
from django.template.response import TemplateResponse
from django.views.generic.list import ListView

from models import News, Event


class NewsList(ListView):
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.filter(is_active=True)


def news_details(request, slug):
    try:
        news = News.objects.filter(is_active=True).get(slug=slug)
    except News.DoesNotExist:
        raise Http404()
    context = {
        'news': news,
    }
    template_name = 'news/news_details.html'
    return TemplateResponse(request, template_name, context)



class EventList(ListView):
    template_name = 'event/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(is_active=True, date_from__gte=datetime.datetime.today()).order_by('date_from')


class EventPastList(ListView):
    template_name = 'event/event_list_past.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(is_active=True, date_from__lt=datetime.datetime.today()).order_by('-date_from')


def event_details(request, slug):
    try:
        event = Event.objects.filter(is_active=True).get(slug=slug)
    except Event.DoesNotExist:
        raise Http404()
    context = {
        'event': event,
    }
    template_name = 'event/event_detail.html'
    return TemplateResponse(request, template_name, context)
