from django.http import Http404
from django.template.response import TemplateResponse
from models import Story, Category
from django.views.generic.detail import DetailView


class CategoryDetail(DetailView):
    template_name = 'stories/category_detail.html'

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


def story_detail(request, category_slug, slug):
    try:
        story = Story.objects.filter(is_active=True).get(slug=slug)
    except Story.DoesNotExist:
        raise Http404()
    context = {
        'story': story,
    }
    template_name = 'stories/story_detail.html'
    return TemplateResponse(request, template_name, context)