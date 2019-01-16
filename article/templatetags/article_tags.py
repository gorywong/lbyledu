#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-10 00:31:51
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-10 00:31:51
@Description:
"""
from django import template
from django.conf import settings
from django.urls import reverse
from article.models import Article, Category, Banner

register = template.Library()

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