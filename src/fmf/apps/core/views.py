from django.views.generic.base import TemplateView

from models import IndexSliderImage, IndexTab
from news.models import News


class IndexView(TemplateView):
    template_name = 'core/index_view.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['images'] = IndexSliderImage.objects.filter(is_active=True)
        context['news_list'] = News.objects.filter(is_active=True, is_main=True)[:3]
        context['tabs'] = IndexTab.objects.all()
        return context
