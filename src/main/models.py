# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Players(db.Model):
    key = db.Key
    firstname = db.StringProperty()
    lastname = db.StringProperty()
    nickname = db.StringProperty()
    country = db.StringProperty()
    attendedyears = db.ListProperty(int)
    testadd = db.StringProperty()
#    pattern = db.ListProperty()
     
class Commentaries(db.Model):
    key = db.Key
    name = db.StringProperty()

#class playpattern(db.Model):

#class commentpattern(db.Model):

#class playphrase(db.Model):


#class tweetrequest(db.Model):
