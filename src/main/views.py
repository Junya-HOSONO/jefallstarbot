# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
import django
import datetime

def index(request):
    #メインページ
    return render_to_response(
        'main/index.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )

def request(request):
    #リクエストページ
    return render_to_response(
        'main/request.html',
        { 'clock': datetime.datetime.now(),
          'dver': ",".join([str(r) for r in django.VERSION]) },
    )

