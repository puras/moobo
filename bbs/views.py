# -*- coding: utf-8 -*-
__author__ = 'puras'

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from bbs.models import Topic, Node, Category

# Create your views here.
def index(req):
    lastest_topic_list = Topic.objects.order_by('-pub_date')[:20]
    context = { 'lastest_topic_list': lastest_topic_list }
    return render(req, 'index.html', context)

def topic(req, topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)
    return render(req, 'topic.html', {'topic': topic})