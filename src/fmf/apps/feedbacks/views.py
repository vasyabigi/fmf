from django.http import Http404
from django.template.response import TemplateResponse

from feedbacks.models import Feedback


def feedbacks_list(request):
    feedbacks = Feedback.objects.all()
    context = {'feedbacks': feedbacks, }
    return TemplateResponse(request, 'feedbacks/feedback_list.html', context)


def feedback_details(request, slug):
    try:
        feedback = Feedback.objects.get(slug=slug)
    except Feedback.DoesNotExist:
        raise Http404()
    else:
        context = {'feedback': feedback, }
        return TemplateResponse(request, 'feedbacks/feedback_details.html', context)
