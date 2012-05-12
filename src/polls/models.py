#from django.db import models
# -*- coding: utf-8 -*-
#
#class Poll(models.Model):
#    question = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#
#class Choice(models.Model):
#    poll = models.ForeignKey(Poll)
#    choice = models.CharField(max_length=200)
#    votes = models.IntegerField()

from google.appengine.ext import db

class Poll(db.Model):
    iid = db.IntegerProperty(required=True)
    question = db.StringProperty(required=True)
    pub_date = db.DateTimeProperty(auto_now_add=True)
    def __unicode__(self):
        return self.question

class Choice(db.Model):
    iid = db.IntegerProperty(required=True)
    poll_id = db.ReferenceProperty(Poll,collection_name='choices')
    choice = db.StringProperty(required=True)
    votes = db.IntegerProperty(required=True)
    def __unicode__(self):
        return self.choice    
    


#下の２行でデータストアに登録可能、ただし日付はUTC？
#obj = Poll(iid=1,question=u"それはなに？")
#obj = Poll(iid=2,question=u"それはなに？1")
#obj2 = Poll(iid=3,question=u"それはなに？2")
#obj.put()
#obj2.put()

#q = db.Query(Poll).filter('iid =', 1)
#p1 = q.get()
#c1 = Choice(iid=1001,poll_id=p1.key(), choice="dog",votes=0)
#c2 = Choice(iid=1001,poll_id=p1.key(), choice="cat",votes=1)
#c1.put()
#c2.put()

