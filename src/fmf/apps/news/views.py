from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from news.models import News


class NewsList(ListView):
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.filter(is_active=True)


class NewsDetails(DetailView):
    template_name = 'news/news_details.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_active=True)