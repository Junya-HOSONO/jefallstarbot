# -*- coding: utf-8 -*-

#ここでテストデータを一気にインポートする

#10選手、3プレイくらいずつ

#from google.appengine.ext import db
from mainapp import models
import pickle
import logging


#------------------------プレイリスト登録-------------------------

#全件削除
q = models.PlayList.all()
for playlist in q:
    playlist.delete()

plist = models.PlayList()
plist.playlist_id = 1
plist.plays = ["0AT05SP0600","1AT06CR0201","1AT02HS1011"]
plist.endplay = 3
plist.goal = True
plist.lost = False
plist.goodplay = 2
plist.put()

plist2 = models.PlayList()
plist2.playlist_id = 2
plist2.plays = ["0AT05SP0400","1AT04CR0201","1AT02HS1011"]
plist2.endplay = 3
plist2.goal = False
plist2.lost = False
plist2.goodplay = 1
plist2.put()


#------------------------選手登録-------------------------

#全件削除
q = models.Player.all()
for player in q:
    player.delete()

obj = models.Player()
obj.firstname = u"勇樹"
obj.lastname = u"阿部"
obj.lastname_kana = u"アベ"
obj.nickname = u"阿部ちゃん"
obj.country = u"日本"
obj.attendedyear = [2003,2004,2005,2006]
obj.attendedyear.append(2007) #OK
obj.wikiurl = u"http://ja.wikipedia.org/wiki/%E9%98%BF%E9%83%A8%E5%8B%87%E6%A8%B9"
obj.play = ["0AT05SP0600","0DF08IS0200"]
obj.playdict = pickle.dumps({
'0AT05SP0600' : u'…中盤でボールを受けた_own_がすかさず右サイドの_next_にパス！',
'0DF08IS0200' : u'…ペナルティエリア内まで戻った_own_がボールを奪って素早く前線にロングフィード！'
})
obj.put()

obj2 = models.Player()
obj2.firstname = u"誠一郎"
obj2.lastname = u"巻"
obj2.lastname_kana = u"マキ"
obj2.nickname = u"マキ"
obj2.country = u"日本"
obj2.attendedyear = [2003,2004,2005,2006,2007,2008,2009,2010]
obj2.wikiurl = u"http://ja.wikipedia.org/wiki/%E5%B7%BB%E8%AA%A0%E4%B8%80%E9%83%8E"
obj2.play = ["1AT02HS1011"]
obj2.playdict = pickle.dumps({
'1AT02HS1011' : u'それを_own_がヘッドでゴール右隅に叩き込んだ！ゴール！'
})
obj2.put()

obj4 = models.Player()
obj4.firstname = u"コウキ"
obj4.lastname = u"水野"
obj4.lastname_kana = u"ミズノ"
obj4.nickname = u"水野"
obj4.country = u"日本"
obj4.attendedyear = [2005,2006,2007]
obj4.play = ["1AT06CR0201"]
obj4.playdict = pickle.dumps({
'1AT06CR0201' : u'_own_がトラップと同時にルックアップ、速いクロスをゴール前へ！'
})
obj4.put()

obj3 = models.Player()
obj3.firstname = u"昌弘"
obj3.lastname = u"岡本"
obj3.lastname_kana = u"オカモト"
obj3.nickname = u"グッピー"
obj3.country = u"日本"
obj3.attendedyear = [2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]
obj3.put()

#現在の選手
#深井
#ヨネ
#兵働
#谷澤
#サトケン
#藤田
#ユースケ
#大介
#櫛野
#大岩
#武田
#オーロイ
#渡辺
#坂本
#勇人
#町田
#竹内
#山口智
#青木りょうた
#ロボ



#昔の
#ネット
#アレックス
#ミリガン
#ストヤノフ
#立石
#青木孝太
#工藤浩平
#齊藤大介
#茶の
#水本
#ボスナー
#池田招聘
#下村

#観たこと無いひと
#ちぇ・よんす
#城しょうじ
#野々村
#リトバルスキー
#江尻
#マスロバル
#オッツェ
#パベル
#山岸
#下川
#武藤真一
#中西永輔
#ミリノビッチ
#ポペスク
#林
#バロン
#ハース
#村井
#新井
#中島浩司
#村井
#羽生
#楽山
#結城
#益山
#ボス
#戸田
#ミシェウ
#
#
#
#
#

