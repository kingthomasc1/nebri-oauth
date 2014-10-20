from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^smartthings/oauth/authorize/$',
        'smartthings.views.oauth_authorize',
        name='Smart Things authorize'),
    url(r'^smartthings/oauth/callback/(?P<client_id>[^/]+)/(?P<client_secret>[^/]+)/(?P<instance_inbox>[^/]+)/'
        r'(?P<instance_name>[^/]+)/(?P<sender>[^/]+)/$',
        'smartthings.views.oauth_callback',
        name='Smart Things callback'),
)
