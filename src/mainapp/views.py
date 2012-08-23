# -*- coding: utf-8 -*-

# Create your views here.

#from django.http import HttpResponse
#
#def home(request):
#    return HttpResponse('The Book Store home page.')

from django.shortcuts import render_to_response
import django
import datetime
import logging
from dateutil import zoneinfo, tz


#from models import Tweet
from models import Tweet

def home(request):
    logging.info('mainapp home start')
    return render_to_response(
        'mainapp/index.html',
        { 'clock': localtime(datetime.datetime.now(tz.tzutc())),
#        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )

def tweet(request):
    logging.info('mainapp tweet start')
    t=Tweet()
    t.tweet(request)
    #なにか画面に出す
    return render_to_response(
        'mainapp/index.html',
        { 'clock': "tweeted!",
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )




# 関数

def localtime(dt, tzname='Asia/Tokyo'):
  """
  >>> from datetime import *
  >>> now = datetime.now(tz.tzutc())
  >>> localtime(now)
  """
  return dt.replace(tzinfo=tz.tzutc()).astimezone(zoneinfo.gettz(tzname))
  
  