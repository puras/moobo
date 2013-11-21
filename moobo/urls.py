# -*- coding: utf-8 -*-
__author__ = 'puras'
from django.conf.urls import patterns, include, url
from django.views.static import serve
from django.conf import settings

from bbs.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moobo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='bbs'),
    url(r'^bbs/', include('bbs.urls', namespace='bbs')),
    url(r'^upload/', include('editor.urls', namespace='editor')),
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
        }),
    # url(r'^blog/$', include(blog.urls, namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)
