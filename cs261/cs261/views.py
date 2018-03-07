from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

from history import models

import requests
import json
import os
import datetime

# Where the magic happens.
# i.e. this is where we interface with the app logic.
def query(request):
    q_text = request.GET.get('q', 'No query')
    params = {
        'query': q_text,
        'sessionId': '1',
        'v': '20150910',
        'lang': 'en'
    }

    headers = {
        'Authorization': 'Bearer ' + os.environ['BOT_TOKEN']
    }

    r = requests.get('https://api.dialogflow.com/v1/query', params=params, headers=headers)
    # print(r.text)
    try:
        text = json.loads(r.text)['result']['fulfillment']['speech']
    except KeyError:

        text = 'Something went wrong. Please try again.'

    # store history and file log
    with open('logs/' + datetime.datetime.now().strftime('%Y-%m-%d-T%H-%M-%S.json'), 'w+') as f:
        f.write(json.dumps(r.json(), indent=2))

    intent = None
    try:
        intent = r.json()['result']['metadata']['intentName']
        print('intent:', intent)

        entities = r.json()['result']['parameters']
        print('entities:', entities)
        for i in entities:
            if (type(entities[i]) != list):
                continue

            q = models.Query(text=q_text, intent=intent)
            q.save()
            for j in entities[i]:
                entity, created = models.Entity.objects.get_or_create(entity_type=i, name=j)
                q.entities.add(entity)
            q.save()

    except:
        print('error')

    print(text)
    # make response

    context = {
        'message': text
    }

    if intent == 'NewsIntent':
        # TODO: Integrate with scraper
        fakenews = []
        fakenews.append({
            'title': '$company sucks',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'link': 'http://link',
            'publicationdate': '00/00/00'
        })
        fakenews.append({
            'title': 'The value of Aviva is 3',
            'description': 'lorem',
            'link': 'http://link',
            'publicationdate': '11/22/33'
        })
        print(fakenews)
        context['news'] = fakenews

    return render(request, 'cs261/response.html', context=context)
