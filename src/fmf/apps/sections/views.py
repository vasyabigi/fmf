from models import Section, Article
from django.shortcuts import render, get_object_or_404


def section_details(request, slug):
    section = get_object_or_404(Section, slug=slug)
    context = {
        'section': section,
    }
    return render(request, 'sections/section_details.html', context)


def article_details(request, section_slug, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    context = {
        'article': article,
    }
    return render(request, 'sections/article_details.html', context)
