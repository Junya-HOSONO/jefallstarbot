# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'main.views.index')             #トップページ
    (r'^index.html$', 'main.views.index')   #トップページ
    (r'^request$', 'main.views.request')    #リクエストページ
    (r'^tweet$', 'main.views.tweet')        #ツイート
    (r'^testapp/', 'testapp.views.home')
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

