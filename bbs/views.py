# -*- coding: utf-8 -*-
__author__ = 'puras'

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime

from bbs.models import Topic, Node, Category, Reply
from bbs.forms import TopicForm, ReplyForm

# Create your views here.
def index(req):
    lastest_topic_list = Topic.objects.order_by('-pub_date')[:20]
    category_list = Category.objects.all()
    return render(req, 'index.html', {
        'lastest_topic_list': lastest_topic_list,
        'category_list': category_list,
        })

def topic(req, topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)
    reply_form = ReplyForm()
    return render(req, 'topic.html', {'topic': topic, 'reply_form': reply_form})

def topic_create(req, node_id):
    node = get_object_or_404(Node, pk = node_id)
    if req.method == 'POST':
        form = TopicForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tp = Topic.objects.create(
                title = cd['title'],
                content = cd['content'],
                author = req.user,
                category = node.category,
                node = node,
                pub_date = datetime.now(),
            )
            tp.save()
            return HttpResponseRedirect(reverse('bbs:topic', args = (tp.id, )))
    else:
        form = TopicForm()

    return render(req, 'topic/create.html', {'form': form })

def topic_reply(req, topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)
    if req.method == 'POST':
        form = ReplyForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            re = Reply.objects.create(
                content = cd['content'],
                topic = topic,
                author = req.user,
                pub_date = datetime.now(),
            )
            re.save()
            return HttpResponseRedirect(reverse('bbs:topic', args = (topic_id, )))
        else:
            return render(req, 'topic.html', {'topic': topic, 'reply_form': form})


def node(req, node_id):
    node = get_object_or_404(Node, pk = node_id)
    topic_list = Topic.objects.order_by('-pub_date').filter(node_id = node_id)[:20]
    return render(req, 'node.html', { 
        'node': node,
        'topic_list': topic_list
    })

def login(req):
    if req.method == 'POST':
        username = req.POST.get('username', '')
        passwd = req.POST.get('passwd', '')
        user = auth.authenticate(username = username, password = passwd)
        if user is not None and user.is_active:
            auth.login(req, user)
            return HttpResponseRedirect('/')
        else:
            return render(req, 'login.html')

    return render(req, 'login.html')

def logout(req):
    auth.logout(req)
    return HttpResponseRedirect(reverse('bbs:login'))

def join(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        return render(req, 'join.html', { 'form': form, })

def change_password(req):
    if req.method == 'POST':
        old_passwd = req.POST.get('old_passwd', '')
        passwd = req.POST.get('passwd', '')
        repasswd = req.POST.get('repasswd', '')
        if not passwd == repasswd:
            # 传递错误信息,新密码与确认新密码不同
            return render(req, 'password.html', { 'error': None })
        user = req.user
        test_user = auth.authenticate(username = user.username, password = old_passwd)
        if test_user is not None:
            user.set_password(passwd)
            user.save()
            return logout(req)
        else:
            # 传递错误信息，原密码不符
            return render(req, 'password.html')

    else:
        return render(req, 'password.html')