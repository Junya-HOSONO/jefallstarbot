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
from models import Tweet, Player

def home(request):
    logging.info('mainapp home start')
    return render_to_response(
        'mainapp/base-index.html',
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
        'mainapp/base-index.html',
        { 'clock': "tweeted!",
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )

def players(request):
    logging.info('mainapp players start')

    #Player一覧を作る
    q = Player.all()
#    for player in q: #OK
#        logging.info(player.firstname)

#    results = q.fetch() #NG
       
    return render_to_response(
        'mainapp/base-players.html',
        { 'playercount': q.count(), 'playerdata': q },
    )


def aboutthisbot(request):
    logging.info('mainapp aboutthisbot start')

    try:
        return render_to_response(
            'mainapp/base-aboutthisbot.html',
            { },
        )
    except Exception, e:
        logging.error(e)     

def testdataload(request):
    logging.info('mainapp testdataload start')

    obj = Player()
    obj.firstname = u"勇樹"
    obj.lastname = u"阿部"
    obj.nickname = u"阿部ちゃん"
    obj.country = u"日本"
    obj.attendedyear = [2003,2004,2005,2006,2007]
    obj.put()

    obj2 = Player()
    obj2.firstname = u"誠一郎"
    obj2.lastname = u"巻"
    obj2.nickname = u"マキ"
    obj2.country = u"日本"
    obj2.attendedyear = [2003,2004,2005,2006,2007,2008,2009,2010]
    obj2.put()
    
    return render_to_response(
        'mainapp/base-players.html',
        {  },
    )


# 関数

def localtime(dt, tzname='Asia/Tokyo'):
  """
  >>> from datetime import *
  >>> now = datetime.now(tz.tzutc())
  >>> localtime(now)
  """
  return dt.replace(tzinfo=tz.tzutc()).astimezone(zoneinfo.gettz(tzname))
  
  