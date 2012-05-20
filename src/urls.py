# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^testapp/', 'testapp.views.home'),
    (r'^index.html', 'mainlogic.views.index'),
    (r'^./$', 'mainlogic.views.index'), #これがうまくいかない
    (r'^request', 'mainlogic.views.request'),
    (r'^tweet', 'mainlogic.views.tweet'),
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

