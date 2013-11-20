# -*- coding: utf-8 -*-
__author__ = 'puras'

from django import forms

class TopicForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs={'size': '100', 'placeholder': '主题标题'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': '100', 'rows': '30', 'placeholder': '主题内容'}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 4:
            raise forms.ValidationError('内容过短')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 4:
            raise forms.ValidationError('内容过短')
        return content

class ReplyForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': '100', 'rows': '10', 'placeholder': '回复内容'}))
    
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 4:
            raise forms.ValidationError('内容过短')
        return content