from django.contrib.flatpages.views import flatpage
from django.http import Http404
from django.template.base import TemplateDoesNotExist
from django.template.loader import find_template
from django.template.response import TemplateResponse

from models import ExtraFlatPage


def custom_flatpage(request, url):
    try:
        page = ExtraFlatPage.objects.get(page__url='/'+url)
    except ExtraFlatPage.DoesNotExist:
        return flatpage(request, url)

    try:
        template_name = 'flatpages_extra/%s.html' % page.page.url.replace('/','')
        find_template(template_name)
    except TemplateDoesNotExist:
        raise Http404()

    return TemplateResponse(request, template_name, {'images': page.images.filter(is_active=True), 'flatpage':page.page })
