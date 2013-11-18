# -*- coding: utf-8 -*-
__author__ = 'puras'

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from bbs.models import Topic, Node, Category

# Create your views here.
def index(req):
    lastest_topic_list = Topic.objects.order_by('-pub_date')[:20]
    context = { 'lastest_topic_list': lastest_topic_list }
    return render(req, 'index.html', context)

def topic(req, topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)
    return render(req, 'topic.html', {'topic': topic})

def login(req):
    if req.method == 'POST':
        username = req.POST.get('username', '')
        passwd = req.POST.get('passwd', '')
        user = auth.authenticate(username = username, password = passwd)
        if user is not None and user.is_active:
            auth.login(req, user)
            # return HttpResponse('You are logged in.')
            return HttpResponseRedirect('/')
        else:
            return render(req, 'login.html')
            # return HttpResponse('You are not logged in.')

    return render(req, 'login.html')
    # if req.method == 'POST':
        # if req.session.test_cookie_worked():
        #     req.session.delete_test_cookie()

        #     return HttpResponse('You are logged in.')
        # else:
        #     return HttpResponse('Please enable cookies and try again.')

    # req.session.set_test_cookie()
    # return render(req, 'login.html')

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
    # if req.method == 'POST':
    #     if req.session.test_cookie_worked():
    #         return HttpResponse('You are sign up ok.')
    #     else:
    #         return HttpResponse('Please enable cookies and try again.')

    # req.session.set_test_cookie()
    # return render(req, 'join.html')