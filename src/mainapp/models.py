# -*- coding: utf-8 -*-

from google.appengine.ext import db
import logging
from extlib import twitterlib
import secretdata
import datetime

class PlayList(db.Model):
    # 一連のプレーをデータ化したもの
    playlist_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    plays = db.ListProperty(basestring)
    endplay = db.IntegerProperty()    
    goal = db.BooleanProperty()
    lost = db.BooleanProperty()
    goodplay = db.IntegerProperty()
    badplay = db.IntegerProperty()   
    
class Tweet():
    logging.info('Tweet start') #あああ
    def tweet(self, request):
        logging.info('tweet start') #あああ
        #ここでつぶやくロジックを入れておく
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
            #つぎやいたものをMyTweetに保管する
            logging.info('tweet finish')
        except Exception, e:
            logging.error(e)        




class Player(db.Model):
    # 選手個人のデータ
    player_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    firstname = db.StringProperty()
    lastname = db.StringProperty()
    attendedyear = db.ListProperty(int)
    nickname = db.StringProperty()
    country = db.StringProperty()
#    
    #UTCで登録してあるデータから日本時間でgetする
    def get_create_time(self):
        return self.create_time + datetime.timedelta(hours=9)    
    def get_last_update(self):
        return self.last_update + datetime.timedelta(hours=9)    
    def get_fullname(self):
        return self.lastname + " " + self.firstname    

class MyTweet(db.Model):
    # 自分がつぶやいたものを保管
    mytweet_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    tweet = db.StringProperty()            #tweetそのもの
    tweeturl = db.StringProperty()         #tweetのurl
    players = db.ListProperty(basestring)  #該当する選手のデータキーのリスト
    commentator = db.Key                   #該当するコメンテーターのデータキー
    request = db.Key                       #リクエストから作られたtweetならそのデータキー
    
    