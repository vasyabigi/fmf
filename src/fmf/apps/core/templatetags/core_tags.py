from django import template

register = template.Library()


@register.filter
def get_random_question(feedback):
    return feedback.questions.filter(is_on_main=True).order_by('?').select_related()[0]