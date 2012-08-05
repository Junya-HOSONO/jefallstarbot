# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^testapp/', 'testapp.views.home'), #OK
    (r'^mainapp/', 'mainapp.views.home'), #OK
    (r'^tweet', 'mainapp.views.tweet'), #OK
    (r'^/', 'testapp.views.home'), #だめ
#    (r'^./$', 'mainlogic.views.index'), #これがうまくいかない
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

