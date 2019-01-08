# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

# Create your models here.

class SuperModules(models.Model):
    name = models.CharField(max_length=20, verbose_name="名称", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "顶级板块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SubModules(models.Model):
    name = models.CharField(max_length=20, verbose_name="名称", default="")
    supermodules = models.ForeignKey(SuperModules, on_delete=models.CASCADE, verbose_name="父板块")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "次级板块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.supermodules.name + '-->' + self.name