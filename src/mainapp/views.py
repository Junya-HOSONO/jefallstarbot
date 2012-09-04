# -*- coding: utf-8 -*-

# Create your views here.

from django.http import HttpResponse
from google.appengine.ext.db import Key
from django.core.context_processors import csrf

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

def tweet_fromcron(request):
    #
    logging.info('mainapp tweet_fromcron start')
    #
    tweet(request)
    return 


def tweet(request):
    logging.info('mainapp tweet start')
    t=Tweet()
    t.tweet(request)
    #なにか画面に出す
    logging.info('mainapp tweet end')

    return render_to_response(
        'mainapp/base-index.html',
        {  },
    )

def players(request):
    logging.info('mainapp players start')

    #Player一覧を作る
    q = Player.all()
       
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

    import testdata
    
    return render_to_response(
        'mainapp/base-players.html',
        {  },
    )



def getajax(request):
    logging.info('called getajax')

    if request.is_ajax():
        if request.method == "POST":
            logging.info('getajax start')
            parm = request.POST #POSTの引数のみを参照する
            parm_key = parm['key']
#            logging.info(parm_key)

            #responseオブジェクトを準備
            res = HttpResponse(mimetype='application/json')
            res['Pragma'] = 'no-cache'

            #返すデータをJSONで生成
            keyobj = Key(parm_key)
            pl = Player.get(keyobj)
            if pl:
                #引数で指定されたキーを持つ選手の、とりあえず名前を返す
                retstr = u""
                logging.info(pl.get_fullname())
#                retstr = '{ "name" : "' + pl.get_fullname() + '"}' #OK
                retstr = '{"graphset" : [{"type" : "bar","series" : [{"values" : [' + str(pl.get_playcount()) + ']}]}]}'
                logging.info(retstr)
                res.write(retstr)

            logging.info('getajax end')
            return res

        logging.info('illegal access to getajax')
        #エラー画面を返す？
        return 
            
    else:
        logging.info('illegal access to getajax')
        #エラー画面を返す？
        return 

# 関数

def localtime(dt, tzname='Asia/Tokyo'):
  """
  >>> from datetime import *
  >>> now = datetime.now(tz.tzutc())
  >>> localtime(now)
  """
  return dt.replace(tzinfo=tz.tzutc()).astimezone(zoneinfo.gettz(tzname))
  
  