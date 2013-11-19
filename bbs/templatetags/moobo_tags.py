# -*- coding: utf-8 -*-
__author__ = 'puras'

from django.template import Library

from bbs.helper import tl_markdown

register = Library()


@register.filter
def md(_md):
    return tl_markdown(_md)