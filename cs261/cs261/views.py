from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

# Where the magic happens.
# i.e. this is where we interface with the app logic.
def query(request):
    context = {
        'query': request.GET.get('q', '?')
    }
    print(context)
    return render(request, 'cs261/response.html', context=context)
