# -*- coding: utf-8 -*-

from google.appengine.ext import db
from extlib import twitterlib
import secretdata
import logging


class Tweet():
    #ここでつぶやくロジックを入れておく
    def tweet(self, request):
        try:
            #twitter準備
            logging.info('tweet start')
            ctok, csec = secretdata.TWITTER_CONSUMER_KEY, secretdata.TWITTER_CONSUMER_SECRET
            auth = twitterlib.TwitterOAuth(ctok, csec, use_https=True)
            atok,asec = secretdata.TWITTER_ACCESS_TOKEN_KEY, secretdata.TWITTER_ACCESS_TOKEN_SECRET
            auth.setAccessToken(atok, asec)
            api = twitterlib.API(auth)
            #URL解析、パスワードあるかどうか
            #つぶやく
            api.statuses.update(status=u'aaa!')
            logging.info('tweet finish')
        except Exception, e:
            logging.error(e)            

class Players(db.Model):
#    key = db.Key
    firstname = db.StringProperty()
#    lastname = db.StringProperty()
#    nickname = db.StringProperty()
#    country = db.StringProperty()
#    attendedyears = db.ListProperty(int)
#    testadd = db.StringProperty()
#    pattern = db.ListProperty()
     
#class Commentaries(db.Model):
#    key = db.Key
#    name = db.StringProperty()

#class playpattern(db.Model):

#class commentpattern(db.Model):

#class playphrase(db.Model):


#class tweetrequest(db.Model):

