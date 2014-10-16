from django.core.mail import send_mail
from django.shortcuts import render, redirect
import requests


def oauth_authorize(request):
    client_id = request.GET['client_id']
    client_secret = request.GET['client_secret']
    instance_inbox = request.GET['instance_inbox']
    redirect_uri = 'http://%s/smartthings/oauth/callback/%s/%s/%s/' % (request.get_host(), client_id, client_secret, instance_inbox)
    return redirect('https://graph.api.smartthings.com/oauth/authorize?response_type=code&client_id=%s&scope=app&redirect_uri=%s' % (client_id, redirect_uri))


def oauth_callback(request, client_id, client_secret, instance_inbox):
    code = request.GET['code']
    redirect_uri = 'http://%s/smartthings/oauth/callback/%s/%s/%s/' % (request.get_host(), client_id, client_secret, instance_inbox)
    response = requests.get('https://graph.api.smartthings.com/oauth/token?grant_type=authorization_code&client_id=%s&client_secret=%s&redirect_uri=%s&scope=app&code=%s' % (client_id, client_secret, redirect_uri, code))
    send_mail('', 'st_access_token := %s' % response.json()['access_token'], 'tomk@bixly.com', [instance_inbox], fail_silently=False)
    return redirect('https://nebrios.com')