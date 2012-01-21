# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

from importpath import importpath
from models import Seo, Url

from modeltranslation.admin import TranslationGenericStackedInline


class SeoInlines(TranslationGenericStackedInline):
    model = Seo
    extra = 1
    max_num = 1

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }


class UrlAdmin(admin.ModelAdmin):
    model = Url
    inlines = [SeoInlines]

admin.site.register(Url, UrlAdmin)


if not hasattr(settings, 'SEO_FOR_MODELS'):
    raise ImproperlyConfigured('Please add ``SEO_FOR_MODELS = ["<app>.admin.<ModelAdmin>",]`` to your settings.py')

for model_name in settings.SEO_FOR_MODELS:
    model = importpath(model_name, 'SEO_FOR_MODELS')
    try:
        model_admin = admin.site._registry[model].__class__
    except KeyError:
        raise ImproperlyConfigured('Please set ``seo`` in your settings.py only as last INSTALLED_APPS')
    admin.site.unregister(model)

    setattr(model_admin, 'inlines', getattr(model_admin, 'inlines', []))
    if not SeoInlines in model_admin.inlines:
        model_admin.inlines = list(model_admin.inlines)[:] + [SeoInlines]

    admin.site.register(model, model_admin)
