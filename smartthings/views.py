from django.core.mail import send_mail
from django.shortcuts import render, redirect
import requests


def oauth_authorize(request):
    client_id = request.GET['client_id']
    client_secret = request.GET['client_secret']
    instance_inbox = request.GET['instance_inbox']
    instance_name = request.GET['instance_name']
    sender = request.GET['sender']
    redirect_uri = 'http://%s/smartthings/oauth/callback/%s/%s/%s/%s/%s/' % (request.get_host(), client_id,
                                                                             client_secret, instance_inbox,
                                                                             instance_name, sender)
    return redirect('https://graph.api.smartthings.com/oauth/authorize?response_type=code&client_id=%s&scope=app'
                    '&redirect_uri=%s' % (client_id, redirect_uri))


def oauth_callback(request, client_id, client_secret, instance_inbox, instance_name, sender):
    code = request.GET['code']
    instance_url = 'https://%s.nebrios.com/interact' % instance_name
    redirect_uri = 'http://%s/smartthings/oauth/callback/%s/%s/%s/%s/%s/' % (request.get_host(), client_id,
                                                                             client_secret, instance_inbox,
                                                                             instance_name, sender)
    response = requests.get('https://graph.api.smartthings.com/oauth/token?grant_type=authorization_code&client_id=%s&'
                            'client_secret=%s&redirect_uri=%s&scope=app&code=%s' % (client_id, client_secret,
                                                                                    redirect_uri, code))
    send_mail('', 'st_access_token := %s' % response.json()['access_token'], sender, [instance_inbox],
              fail_silently=False)
    return redirect(instance_url)