# -*- coding: utf-8 -*-
__author__ = 'puras'

from django.conf.urls import patterns, url

from .views import ke_upload, ke_man

urlpatterns = patterns('',
    url(r'^ke_upload/$', ke_upload, name='ke_upload'),
    url(r'^ke_man/$', ke_upload, name='ke_man'),
)