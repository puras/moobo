# -*- coding: utf-8 -*-
__author__ = 'puras'

from django.conf.urls import patterns, url
from bbs import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^join/$', views.join, name='join'),
)