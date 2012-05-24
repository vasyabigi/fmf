import datetime
from django.http import Http404
from django.template.response import TemplateResponse
from django.views.generic.list import ListView
from django.shortcuts import render

from models import News, Event


def news_list(request):
    context = {
        'news_list': News.objects.filter(is_active=True)
    }
    return render(request, 'news/news_list.html', context)


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
        return Event.objects.filter(is_active=True, date_to__gte=datetime.datetime.today()).order_by('-date_to')


class EventPastList(ListView):
    template_name = 'event/event_list_past.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(is_active=True, date_to__lt=datetime.datetime.today()).order_by('-date_to')


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
