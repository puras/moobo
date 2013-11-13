# -*- coding: utf-8 -*-
__author__ = 'puras'
from django.db import models

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
    node = models.ForeignKey(Node)
    pub_date = models.DateTimeField('发布时间')

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '主题'

    def __unicode__(self):
        return self.title
