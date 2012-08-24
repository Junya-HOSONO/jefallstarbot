# -*- coding: utf-8 -*-

from google.appengine.ext import db
from extlib import twitterlib
import secretdata
import logging
import datetime

class Tweet():
    logging.info('tweet start')

    #ここでつぶやくロジックを入れておく
#    def tweet(self, request):
#        try:
#            #twitter準備
#            logging.info('tweet start')
#            ctok, csec = secretdata.TWITTER_CONSUMER_KEY, secretdata.TWITTER_CONSUMER_SECRET
#            auth = twitterlib.TwitterOAuth(ctok, csec, use_https=True)
#            atok,asec = secretdata.TWITTER_ACCESS_TOKEN_KEY, secretdata.TWITTER_ACCESS_TOKEN_SECRET
#            auth.setAccessToken(atok, asec)
#            api = twitterlib.API(auth)
#            #URL解析、パスワードあるかどうか
#            #つぶやく
#            api.statuses.update(status=u'aaa!')
#            #つぎやいたものをMyTweetに保管する
#            logging.info('tweet finish')
#        except Exception, e:
#            logging.error(e)            

class Player(db.Model):
    # 選手個人のデータ
    player_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty(required=True)
    attendedyear = db.ListProperty(required=True)
    nickname = db.StringProperty()
    country = db.StringProperty(required=True)

class MyTweet(db.Model):
    # 自分がつぶやいたものを保管
    mytweet_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    tweet = db.StringProperty(required=True)            #tweetそのもの
    tweeturl = db.StringProperty(required=True)         #tweetのurl
    players = db.ListProperty(required=True)            #該当する選手のデータキーのリスト
    commentator = db.Key                                #該当するコメンテーターのデータキー
    request = db.Key                                    #リクエストから作られたtweetならそのデータキー

class Request(db.Model):
    # twitterからのリクエスト
    request_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    requester = db.StringProperty()                     #リクエストした人のtwitterID
    request_comment = db.StringProperty()               #リクエストされた文章そのもの
    request_player = db.StringProperty()                #リクエストから抜き出した選手名
    request_year = db.IntegerProperty()                 #リクエストから抜き出した年            
    

class PlayList(db.Model):
    # 一連のプレーをデータ化したもの
    playlist_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    plays = db.ListProperty(required=True)
    endplay = db.IntegerProperty(required=True)    
    goal = db.BooleanProperty(required=True)
    lost = db.BooleanProperty(required=True)
    goodplay = db.IntegerProperty()
    badplay = db.IntegerProperty()

    #UTCで登録してあるデータから日本時間でgetする
    def get_created_time(self):
        return self.created_time + datetime.timedelta(hours=9)
    