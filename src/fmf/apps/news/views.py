from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from news.models import News


class NewsList(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'


class NewsDetails(DetailView):
    model = News
    template_name = 'news/news_details.html'
    context_object_name = 'news'
