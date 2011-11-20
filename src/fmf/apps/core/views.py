from django.views.generic.base import TemplateView

from stories.models import Category
from news.models import News


class IndexView(TemplateView):
    template_name = 'core/index_view.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['news'] = News.objects.filter(is_active=True, is_main=True)
        return context
