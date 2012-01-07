import datetime
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView

from models import IndexSliderImage
from forms import ContactForm
from news.models import News, Event


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


class Test404(TemplateView):
    template_name = '404.html'


class Test500(TemplateView):
    template_name = '500.html'

def contacts(request):
    form = ContactForm(request.POST or None)
    if request.POST:
        pass
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'core/contacts.html', context)