# -*- coding: utf-8 -*-

from google.appengine.ext import db
import logging
from extlib import twitterlib
import secretdata
import datetime
import random
import pickle



class PlayList(db.Model):
    # 一連のプレーをデータ化したもの
    playlist_key = db.Key
    playlist_id = db.IntegerProperty()
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    plays = db.ListProperty(basestring)
    endplay = db.IntegerProperty()    
    goal = db.BooleanProperty()
    lost = db.BooleanProperty()
    goodplay = db.IntegerProperty()
    badplay = db.IntegerProperty()

    def get_create_time(self):
        return self.create_time + datetime.timedelta(hours=9)    
    def get_last_update(self):
        return self.last_update + datetime.timedelta(hours=9) 
        
    def defineplaylist(self):
        logging.info('defineplaylist start')
        ret = []
        #今回のプレイリストを決める
        #1:まったくのランダムで決める
        #2:特定の選手をもとに決める
        #3:特定のシーズンをもとに決める
        
        #1：まったくランダムで決める
        
        #乱数を発生させてplaylist_idから選ぶ
        ir = random.randint(1,1)
#        logging.info(ir)
        #  選んだplaylist_idのプレイに該当する選手をまたランダムで選ぶ
        q = PlayList.all().filter("playlist_id =", ir)
        playlist = q.get()
        if playlist:
            #playlist見つかった
#            ret.append(playlist.key())
            ret.append(playlist)
            plays = playlist.plays
            logging.info("対象PlayList_ID: " + str(playlist.playlist_id))
            #選んだplaylistに該当する選手を探す
            allplayers = Player.all()
            for play in plays:
#                logging.info("play=" + play)
                q = Player.gql("WHERE play = '" + play + "'")
                results = q.fetch(10)
#                logging.info("返ってきた選手の数：" + str(len(results)))
                #もし0件なら、のロジックを個々に入れる
                ir = random.randint(0,len(results)-1)
#                logging.info("何番目の選手？：" + str(ir))
                selectedplayer = results[ir]
                logging.info(u"選ばれた選手：" + selectedplayer.get_fullname())
                ret.append(play)
#                ret.append(selectedplayer.key())
                ret.append(selectedplayer)
        
        #  もし該当する選手がいないプレイがあったら、またplaylist_idから選びなおす
        #でも今は有効なのは1だけなのでランダムで１が出たととする
        logging.info('defineplaylist end')
        return ret
        
    
class Tweet():
    logging.info('Tweet start') #あああ
    def tweet(self, request):
        logging.info('tweet start') #あああ
        #ここでつぶやくロジックを入れておく
        try:

            #URL解析、パスワードあるかどうか
            
            #twitter接続
            logging.info('tweet start')
            ctok, csec = secretdata.TWITTER_CONSUMER_KEY, secretdata.TWITTER_CONSUMER_SECRET
            logging.info('tweet 1') 
            auth = twitterlib.TwitterOAuth(ctok, csec, use_https=True)
            logging.info('tweet 2') 
            atok,asec = secretdata.TWITTER_ACCESS_TOKEN_KEY, secretdata.TWITTER_ACCESS_TOKEN_SECRET
            logging.info('tweet 3') 
            auth.setAccessToken(atok, asec)
            logging.info('tweet 4') 
            api = twitterlib.API(auth)
            logging.info('tweet 5') 

            #つぶやく本文を作成
            tweetnote = u""
            pl = PlayList()
            #プレイリスト確定＆選手確定
            #戻り値：リスト　playlistのオブジェクト, 該当プレーとその該当選手のオブジェクト
            pldata = pl.defineplaylist()

            #tweetnote編集
            logging.info(pldata)
            loopmax = 2*(pldata[0].endplay)+2
            for i in range(2, loopmax, 2): 
                logging.info("loop:" + str(i))
#                logging.info(u"tweetnote_pre :" + tweetnote)
                tmp = pldata[i].get_fromplaydict(pldata[i-1])
                #次の選手の名前があるかもしれないので、それを置換
                if i < loopmax-2:
                    tmp = tmp.replace(u"_next_",pldata[i+2].lastname)

                tweetnote += tmp
#                logging.info(u"tweetnote_post :" + tweetnote)

            #本文に他の情報を付与
            # ハッシュタグ #jasb
            # リクエストの場合は、（@＊＊＊さんからのリクエスト「阿部」）
            # 実際に呟いたtweetのURL？→これは呟いた後に確定するので無理
            # 公式サイトのURL http://bit.ly/jasb_
            tweetnote += " #jasb http://bit.ly/jasb_"
            logging.info(u"確定したtweetnote :" + tweetnote)
            logging.info(u"確定したtweetnoteの文字数 :" + str(len(tweetnote)) + u"文字")

            logging.info('tweet pre call') 

            #実際につぶやく            
            #2012/9/4 本番環境では403エラー
            api.statuses.update(status=tweetnote)

            logging.info('tweet post call') 

#            #つぎやいたものをMyTweetに保管する
            mt = MyTweet()
            mt.tweet = tweetnote
            #ほかにも登録する
            mt.put()
            
            logging.info('tweet finish')
        except Exception, e:
            logging.error(e)        




class Player(db.Model):
    # 選手個人のデータ
#    player_key = db.Key
    create_time = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    firstname = db.StringProperty()
    lastname = db.StringProperty()
    lastname_kana = db.StringProperty()
    attendedyear = db.ListProperty(int)
    play = db.ListProperty(basestring)
    playdict = db.BlobProperty()
    nickname = db.StringProperty()
    country = db.StringProperty()
    wikiurl = db.StringProperty()

    #playdictから該当のプレーを自分の名前入りで返す
    def get_fromplaydict(self, arg_playkey):
        dict_ = pickle.loads(self.playdict)
        return dict_[arg_playkey].replace(u"_own_", self.lastname)

    #keyを文字列に変換して返す
    def get_key_by_string(self):
        return str(self.key())

    #登録プレー数を返す
    def get_playcount(self):
        return len(self.play)

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
    


#allplayers = Player.all()
#毎回の呼び出しで全選手のデータを持ってくるのはやりすぎでない？

