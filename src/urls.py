from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^testapp/', 'testapp.views.home'),
    
    # for polls 
    (r'^polls/$', 'polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
        
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

