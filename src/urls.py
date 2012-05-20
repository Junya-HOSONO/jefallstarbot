from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^testapp/', 'testapp.views.home'),
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)

