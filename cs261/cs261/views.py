from django.http import HttpResponse
from django.utils.html import escape

# Where the magic happens.
# i.e. this is where we interface with the app logic.
def query(request):
    # if we're returning all or part of the query, we might need this to stop people XSSing themselves
    escaped_query = escape(request.GET.get('q', ''))

    # we don't escape the full output,
    # so we can still use arbitrary HTML tags in our response
    # which could be useful
    response = """
I don't know how to respond to {}.
    """.format(escaped_query)
    return HttpResponse(response)
