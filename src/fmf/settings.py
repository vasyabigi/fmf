import os
import sys

from django.utils.translation import ugettext_lazy as _

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

sys.path.append(os.path.join(PROJECT_PATH, 'apps'),)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vasyl Stanislavchuk', 'vasyl.stanislavchuk@gmail.com'),
    ('Traceback Me', '606ozfuayi@traceback.me'),
)

MANAGERS = (
    ('Vasyl Stanislavchuk', 'vasyl.stanislavchuk@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}

TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'uk'

LANGUAGES = (
    ('uk', _('Ukrainian')),
    ('en', _('English')),
)

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static_collected')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = ')qxo^m+0hh^m5agkuzjch5_z*2h&5i$6k%padw(7ff$_93aed1'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'flatpages_my.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "core.context_processors.sections",

)

ROOT_URLCONF = 'fmf.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

PROJECT_APPS = (
    'core',
    'news',
    'flatpages_my',
    'feedbacks',
    'sections',

    #Need to be last
    'seo',
)

INSTALLED_APPS = (
    'localeurl',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    #plugins
    'south',
    'django_extensions',
    'sorl.thumbnail',
    'modeltranslation',
    'pagination',
    'filebrowser',
    'tinymce',
    'chunks',
#    'memcache_status',
    'admin_tools',
    'imperavi',

) + PROJECT_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file_logger': {
            'filename': os.path.join(PROJECT_PATH, 'logs', 'fmf.log'),
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 0,
            'level': 'INFO',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'fmf': {
             'handlers': ['file_logger'],
             'level': 'INFO',
         },
    }
}

MODELTRANSLATION_TRANSLATION_REGISTRY = 'core.translations'

PREFIX_DEFAULT_LOCALE = False

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "preview,fullscreen,table,paste",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_buttons1': "fullscreen,|,undo,redo,|,bold,italic,underline,|,justifyleft,justifycenter,justifyright,|,outdent,indent,|,bullist,numlist,|,anchor,link,unlink,image,|,preview,code,|,cleanup,removeformat,|,pastetext,pasteword",
    'theme_advanced_buttons2': "formatselect,tablecontrols",
    'theme_advanced_buttons3': "",
}

try:
    DEBUG_APPS = DEBUG_MIDDLEWARE_CLASSES = tuple()
    from local_settings import *
    INSTALLED_APPS += DEBUG_APPS
    MIDDLEWARE_CLASSES += DEBUG_MIDDLEWARE_CLASSES
except ImportError:
    print "LOCAL SETTINGS COULD NOT BE FOUND!"


#admin_tools
ADMIN_TOOLS_MENU = 'fmf.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'fmf.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fmf.dashboard.CustomAppIndexDashboard'

#seo
SEO_FOR_MODELS = [
    'news.models.News',
    'news.models.Event',
    'flatpages_my.models.FlatPage',
    'feedbacks.models.Feedback',
    'sections.models.Section',
    'sections.models.Article',
]
