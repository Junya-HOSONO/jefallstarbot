MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
#   'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
#    'django.core.context_processors.media',  # 0.97 only.
#    'django.core.context_processors.request',
)
 
INSTALLED_APPS = (
    'testapp',
#    'poll',
#    'newapp',
)
 
ROOT_URLCONF = 'urls'
 
import os
ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)
