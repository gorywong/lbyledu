#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-10 00:31:51
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-10 00:31:51
@Description:
"""
import re
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from django.urls import reverse
from article.models import Article, Category, Banner

register = template.Library()

@register.filter(name='removehtmltags')
def removehtmltags(content):
    content = content.replace(' ', '')
    reg = re.compile(r'<[^>]+>',re.S)
    result = reg.sub('', content)
    return result

@register.filter(name="truncatechinese", is_safe=True)
@stringfilter
def truncatechinese(value, arg):    
    """Truncates a string after a certain number of words including    
    alphanumeric and CJK characters.     
    Argument: Number of words to truncate after.    
    """    
    try:
        bits = []
        for x in arg.split(u':'):
            if len(x) == 0:
                bits.append(None)
            else:
                bits.append(int(x))
        if int(x) < len(value):
            return value[slice(*bits)] + '...'
        return value[slice(*bits)]

    except (ValueError, TypeError):
        return value # Fail silently.

@register.simple_tag
def query(qs, **kwargs):
    """template tag which allows queryset filtering. Usage:
    {% query article author=author as articles %}
    {% for article in articles %}
    ...
    {% endfor %}
    """
    return qs.filter(**kwargs)

@register.simple_tag
def index_query(qs, **kwargs):
    """template tag which allows queryset filtering. Usage:
    {% query article author=author as articles %}
    {% for article in articles %}
    ...
    {% endfor %}
    """
    return qs.filter(**kwargs)[:6]