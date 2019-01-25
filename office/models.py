#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-23 15:15:01
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-23 15:15:01
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
from users.models import UserGroup, UserProfile

logger = logging.getLogger(__name__)

# Create your models here.
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


class Document(BaseModel):
    title = models.CharField(max_length=200, unique=True, verbose_name="标题")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="发布人")
    content = RichTextUploadingField(verbose_name="正文")
    receiver = models.ManyToManyField(UserProfile, related_name="receivers", verbose_name="收件人")
    receiver_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, verbose_name="收件用户组")
    checked_receiver = models.ManyToManyField(UserProfile, blank=True, related_name="checked_documents", verbose_name="已签收的用户")
    number = models.IntegerField(unique=True, verbose_name="编号")

    class Meta:
        verbose_name = "公文"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
        get_latest_by = 'id'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("office:document_detail", kwargs={"number": self.number})