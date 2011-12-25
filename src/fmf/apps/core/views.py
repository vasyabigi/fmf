from django.views.generic.base import TemplateView

from models import IndexSliderImage
from news.models import News, Event

import datetime


class IndexView(TemplateView):
    template_name = 'core/index_view.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'images': IndexSliderImage.objects.filter(is_active=True),
            'news_list': News.objects.filter(is_active=True)[:3],
            'events': Event.objects.filter(is_active=True, date_to__gte=datetime.datetime.today()).order_by('-date_to')[:3]
        })
        return context
