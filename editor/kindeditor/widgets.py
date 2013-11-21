# -*- coding: utf-8 -*-
__author__ = 'puras'

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class KindEditor(forms.Textarea):
    class Media:
        css = {
            'all': (
                settings.MEDIA_URL + 'editor/kindeditor-4.1.9/themes/default/default.css',
                settings.MEDIA_URL + 'editor/kindeditor-4.1.9/plugins/code/prettify.css',
                ),
        }

        js = (
            "%seditor/kindeditor-4.1.9/kindeditor.js" % settings.MEDIA_URL,
            settings.MEDIA_URL + 'editor/kindeditor-4.1.9/plugins/code/prettify.js',
            )

    def __init(self, attrs = {}):
        super(KindEditor, self).__init__(attrs)

    def render(self, name, value, attrs = None):
        rendered = super(KindEditor, self).render(name, value, attrs)
        context = {
            'name': name,
            'MEDIA_URL': settings.MEDIA_URL,
        }
        return rendered + mark_safe(render_to_string('editor/kindeditor.html', context))