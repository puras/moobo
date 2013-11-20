# -*- coding: utf-8 -*-
__author__ = 'puras'

from django import forms

class TopicForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs={'size': '100', 'placeholder': '主题标题'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': '100', 'rows': '30', 'placeholder': '主题内容'}))

class ReplyForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': '100', 'rows': '10', 'placeholder': '回复内容'}))