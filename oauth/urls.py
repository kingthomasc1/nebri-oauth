from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^smartthings/oauth/authorize/$',
        'smartthings.views.oauth_authorize',
        name='Smart Things authorize'),
    url(r'^smartthings/oauth/callback/(?P<client_id>[^/]+)/(?P<client_secret>[^/]+)/(?P<instance_inbox>[^/]+)/(?P<instance_name>[^/]+)/$',
        'smartthings.views.oauth_callback',
        name='Smart Things callback'),
)
