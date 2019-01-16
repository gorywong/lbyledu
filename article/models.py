#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 12:35:51
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 12:35:51
@Description:
"""
import logging
from abc import abstractmethod

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField

from lbyledu.utils import cache_decorator, cache
from organization.models import Organization

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(default=now, verbose_name="创建时间")
    last_mod_time = models.DateTimeField(default=now, verbose_name="修改时间")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    @abstractmethod
    def get_absolute_url(self):
        pass
    


class Article(BaseModel):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表')
    )
    title = models.CharField(max_length=200, unique=True, verbose_name="标题")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, limit_choices_to={'parent_category__isnull': False}, verbose_name="分类")
    author = models.CharField(max_length=50, verbose_name="作者")
    origin = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="单位")
    content = RichTextUploadingField(verbose_name="正文")
    pub_date = models.DateTimeField(default=now, verbose_name="发布时间")
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='p', verbose_name="文章状态")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    has_check = models.BooleanField(default=False, verbose_name="是否通过审核")
    is_banner = models.BooleanField(default=False, verbose_name="是否用于首页轮播图")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-pub_date']
        get_latest_by = 'id'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail_by_id', kwargs={
            'article_id': self.id,
            'year': self.created_time.year,
            'month': self.created_time.month,
            'day': self.created_time.day
        })

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk))

    def next_article(self):
        return Article.objects.filter(id__gt=self.id, category=self.category, status='p', has_check=True).order_by('id').first()

    def prev_article(self):
        return Article.objects.filter(id__lt=self.id, category=self.category, status='p', has_check=True).order_by('-id').first()


class Category(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name="分类名")
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, limit_choices_to={'parent_category__isnull': True}, related_name='+', verbose_name="父级分类")
    default_child_category = models.ForeignKey('self', blank=True, null=True, limit_choices_to={'parent_category__isnull': False}, related_name='+', on_delete=models.CASCADE, verbose_name="默认子类")

    class Meta:
        ordering = ['id']
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.parent_category:
            return self.parent_category.name + '-->' + self.name
        else:
            return self.name

    def get_absolute_url(self):
        if self.parent_category:
            parent_id = self.parent_category.id
            child_id = self.id
        else:
            parent_id = self.id
            child_id = self.default_child_category.id
        return reverse('article:category_detail', kwargs={
            'parent_id': parent_id,
            'child_id': child_id
        })


class Banner(BaseModel):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, limit_choices_to={'is_banner': True}, verbose_name="轮播图文章")
    image = models.ImageField(upload_to='banner/%Y/%m', max_length=100, verbose_name="轮播图照片")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class SiteSetting(models.Model):
    sitename = models.CharField(max_length=200, null=False, blank=False, default='', verbose_name="网站名称")
    site_description = models.TextField(max_length=1000, null=False, blank=False, default='', verbose_name="网站描述")
    site_seo_description = models.TextField(max_length=1000, null=False, blank=False, default='', verbose_name="网站SEO描述")
    site_keywords = models.TextField(max_length=1000, null=False, blank=False, default='', verbose_name="网站关键字")
    article_sub_length = models.IntegerField(default=250, verbose_name="文章摘要长度")
    beiancode = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="备案号")
    analyticscode = models.TextField(max_length=1000, null=False, blank=False, default='', verbose_name="网站统计代码")
    show_gongan_code = models.BooleanField(default=False, null=False, verbose_name="是否显示公安备案号")
    gongan_beiancode = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name="公安备案号")

    class Meta:
        verbose_name = '网站配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename

    def clean(self):
        if SiteSetting.objects.exclude(id=self.id).count():
            raise ValidationError("只能有一个配置")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from lbyledu.utils import cache
        cache.clear()