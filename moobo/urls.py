# -*- coding: utf-8 -*-
__author__ = 'puras'
from django.conf.urls import patterns, include, url

from bbs.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moobo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^bbs/$', include('bbs.urls', namespace='bbs')),
    # url(r'^blog/$', include(blog.urls, namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)
