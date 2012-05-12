from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^testapp/', 'testapp.views.home'),
    
    # for polls 
    (r'^polls/', include('polls.urls')),
        
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

