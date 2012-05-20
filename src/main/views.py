# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from google.appengine.ext import db
import django
import datetime
#from models import Players
import logging

def index(request):
    return render_to_response(
        'main/index.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )

def request(request):
    return render_to_response(
        'main/request.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )


def tweet(request):
    return render_to_response(
        'main/index.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )
