from django.contrib.flatpages.views import flatpage
from django.template.base import TemplateDoesNotExist
from django.template.response import TemplateResponse
from django.views.generic.create_update import redirect

from models import ExtraFlatPage


def custom_flatpage(request, url):
    try:
        page = ExtraFlatPage.objects.get(page__url='/'+url)
    except ExtraFlatPage.DoesNotExist:
        return flatpage(request, url)

    template_name = 'flatpages_extra/%s.html' % page.page.url.replace('/','')
    return TemplateResponse(request, template_name, {'images': page.images.all(), 'flatpage':page.page })
