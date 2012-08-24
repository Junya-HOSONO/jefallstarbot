# -*- coding: utf-8 -*-

#ここでテストデータを一気にインポートする

#10選手、3プレイくらいずつ

#from google.appengine.ext import db
from mainapp import models

obj = models.Player()
obj.firstname = u"勇樹"
obj.lastname = u"阿部"
obj.nickname = u"阿部ちゃん"
obj.country = u"日本"
obj.attendedyear = [2003,2004,2005,2006,2007]
obj.put()

obj2 = models.Player()
obj2.firstname = u"誠一郎"
obj2.lastname = u"巻"
obj2.nickname = u"マキ"
obj2.country = u"日本"
obj2.attendedyear = [2003,2004,2005,2006,2007,2008,2009,2010]
obj2.put()
