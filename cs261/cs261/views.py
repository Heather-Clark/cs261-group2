from django.http import HttpResponse

# Where the magic happens.
# i.e. this is where we interface with the app logic.
def query(request):
    return HttpResponse('I don\'t know how to respond to "' + request.GET.get('q') + '".')
