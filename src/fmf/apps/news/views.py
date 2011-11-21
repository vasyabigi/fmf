from django.http import Http404
from django.template.response import TemplateResponse
from django.views.generic.list import ListView

from news.models import News


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
