# -*- coding: utf-8 -*-
__author__ = 'puras'

from django import forms
from editor.kindeditor.widgets import KindEditor

class TopicForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs={'size': '90', 'placeholder': '主题标题'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': '90', 'rows': '20', 'placeholder': '主题内容'}))
    content = forms.CharField(widget=KindEditor(attrs={'cols': '90', 'rows': '20', 'placeholder': '主题内容'}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) < 4:
            raise forms.ValidationError('内容过短')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content.strip()) < 4:
            raise forms.ValidationError('内容过短')
        return content

class ReplyForm(forms.Form):
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': '90', 'rows': '10', 'placeholder': '回复内容'}))
    content = forms.CharField(widget=KindEditor(attrs={'class': 'form-control highlight', 'rows': '3', 'placeholder': '回复内容'}))

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content.strip()) < 4:
            raise forms.ValidationError('内容过短')
        return content