# Create your views here.

#from django.http import HttpResponse
#
#def home(request):
#    return HttpResponse('The Book Store home page.')

from django.shortcuts import render_to_response
import django
import datetime

def home(request):
    return render_to_response(
        'testapp/index.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )


