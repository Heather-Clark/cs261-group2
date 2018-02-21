from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

import requests
import json
import os

# Where the magic happens.
# i.e. this is where we interface with the app logic.
def query(request):

    params = {
        'query': request.GET.get('q', 'No query'),
        'sessionId': '1',
        'v': '20150910',
        'lang': 'en'
    }

    headers = {
        'Authorization': 'Bearer ' + os.environ['BOT_TOKEN']
    }

    r = requests.get('https://api.dialogflow.com/v1/query', params=params, headers=headers)

    text = json.loads(r.text)['result']['fulfillment']['speech']

    context = {
        'message': text
    }

    import datetime
    with open('logs/' + datetime.datetime.now().strftime('%Y-%m-%d-T%H-%M-%S.json'), 'w+') as f:
        f.write(r.text)


    return render(request, 'cs261/response.html', context=context)
