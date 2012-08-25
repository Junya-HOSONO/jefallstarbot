# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
#import testdata

urlpatterns = patterns('',
#    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/css'}),
    (r'^testapp/', 'testapp.views.home'), #OK
    (r'^mainapp/', 'mainapp.views.home'), #OK
    (r'^tweet', 'mainapp.views.tweet'), #OK
    (r'^players', 'mainapp.views.players'), #OK
    (r'^testdataload', 'mainapp.views.testdataload'), #OK
    (r'^aboutthisbot', 'mainapp.views.aboutthisbot'), #OK
#    (r'^./$', 'mainlogic.views.index'), #これがうまくいかない
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

