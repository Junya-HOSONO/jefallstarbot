#from django.db import models
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
    question = db.StringProperty(required=True)
    pub_date = db.DateTimeProperty(auto_now_add=True)

class Choice(db.Model):
    poll_id = db.ReferenceProperty(Poll,collection_name='choices')
    choice = db.StringProperty(required=True)
    votes = db.IntegerProperty(required=True)
    