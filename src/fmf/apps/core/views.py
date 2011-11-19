from django.views.generic.base import TemplateView
from stories.models import Category


class IndexView(TemplateView):
    template_name = 'core/index_view.html'
