# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Poll, Choice
from google.appengine.ext import db

def index(request):
    latest_poll_list = Poll.all().order('pub_date')
    return render_to_response(
        'polls/index.html',{'latest_poll_list': latest_poll_list}
    )
    
def detail(request, poll_id):
    q = db.Query(Poll).filter('iid =', int(poll_id))
    p = q.get()
    if p:
        return render_to_response('polls/detail.html', {'poll': p})
        
def vote(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
    q = db.Query(Poll).filter('iid =', int(poll_id))
    p = q.get()
    selected_choice = p.choices.get(iid=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls.views.results', args=(p.iid,)))

#    try:
#    except (KeyError, Choice.DoesNotExist):
#        # Poll 投票フォームを再表示します。
#        return render_to_response('polls/detail.html', {
#            'poll': p,
#            'error_message': u"選択肢を選んでいません。",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # ユーザが Back ボタンを押して同じフォームを提出するのを防ぐ
#        # ため、POST データを処理できた場合には、必ず
#        # HttpResponseRedirect を返すようにします。
#        return HttpResponseRedirect(reverse('polls.views.results', args=(p.iid,)))

def results(request, poll_id):
    q = db.Query(Poll).filter('iid =', int(poll_id))
    p = q.get()
    if p:
        return render_to_response('polls/results.html', {'poll': p})
