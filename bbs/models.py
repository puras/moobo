# -*- coding: utf-8 -*-
__author__ = 'puras'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __unicode__(self):
        return self.name

class Node(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = '节点'

    def __unicode__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=1024, verbose_name='标题')
    content = models.TextField('内容')
    author = models.ForeignKey(User)
    node = models.ForeignKey(Node)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField('发布时间')

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '主题'

    def __unicode__(self):
        return self.title

    def last_reply(self):
        reply = self.reply_set.all().order_by('-pub_date')[:1]
        if reply:
            return reply[0]
        else:
            return None

    def reply_count(self):
        return len(self.reply_set.all())

class Reply(models.Model):
    content = models.TextField('内容')
    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField('发布时间')

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = '回复'

    def __unicode__(self):
        return self.content