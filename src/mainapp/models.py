# -*- coding: utf-8 -*-

import logging
from extlib import twitterlib
import secretdata

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
    