#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 12:40:24
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 12:40:24
@Description:
"""
import logging
from hashlib import md5

from django.core.cache import cache


logger = logging.getLogger(__name__)


def get_md5(str):
    m = md5(str.encode('utf-8'))
    return m.hexdigest()

def cache_decorator(expiration=3 * 60):
    def wrapper(func):
        def news(*args, **kwargs):
            key = ''
            try:
                view = args[0]
                key = view.get_cache_key()
            except:
                key = None
                pass
            if not key:
                unique_str = repr((func, args, kwargs))
                m = md5(unique_str.encode('utf-8'))
                key = m.hexdigest()
            value = cache.get(key)
            if value:
                return value
            else:
                logger.info('cache_decorator set cache:%s key:%s' % (func.__name__, key))
                value = func(*args, **kwargs)
                cache.set(key, value, expiration)
                return value

        return news
    return wrapper


# @cache_decorator
# def get_current_site():
#     site = Site.objects.get_current()
#     return site


# def send_email(emailto, title, content):
#     from DjangoBlog.blog_signals import send_email_signal
#     send_email_signal.send(send_email.__class__, emailto=emailto, title=title, content=content)


def get_site_setting():
    value = cache.get('get_site_setting')
    if value:
        return value
    else:
        from article.models import SiteSettings
        if not SiteSettings.objects.count():
            setting = SiteSettings()
            setting.sitename = "灵宝市豫灵镇中心学校"
            setting.site_description = "基于Django的网上办公系统"
            setting.site_seo_description = "基于Django的网上办公系统"
            setting.site_keywords = "灵宝市豫灵镇中心学校, 事业单位, 网上办公"
            setting.article_sub_length = 122
            setting.beiancode = ''
            setting.analyticscode = ''
            setting.show_gongan_code = False
            setting.gongan_beiancode = ''
            setting.save()
        value = SiteSettings.objects.first()
        logger.info('set cache get_blog_setting')
        cache.set('get_blog_setting', value)
        return value
