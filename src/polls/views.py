#from django.http import HttpResponse
#
#def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")

from django.shortcuts import render_to_response, get_object_or_404
from jefallstarbot.polls.models import Poll

def index(request):
    return render_to_response(
        'polls/index.html',
    )
    
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})
