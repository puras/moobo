# -*- coding: utf-8 -*-
__author__ = 'puras'

from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

import markdown

def tl_markdown(md):
    ret = markdown.markdown(force_unicode(md), 
        ['fenced_code', 'codehilite'], safe_model = False)
    return mark_safe(ret)