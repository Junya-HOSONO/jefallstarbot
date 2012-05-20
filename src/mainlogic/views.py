# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render_to_response
import django
import datetime

def index(request):
    #メインページ
    return render_to_response(
        'mainlogic/index.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )

def request(request):
    #リクエストページ
    return render_to_response(
        'mainlogic/request.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )


