# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import chain
from django.db import models
from tools.storage import ImageStorage
from WeChatDev.basemodels import BaseModel
import django

class KeywordReply(BaseModel):
    """关键词回复"""
    inputDate = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=50, verbose_name='关键字',default='')
    content = models.TextField(null=False, default='')

class Infomation(BaseModel):
    """用户消息"""
    userId = models.CharField(max_length=50, default='')
    inputDate = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images', null=False, default='', storage=ImageStorage())
    text= models.TextField(null=False, default='')

class DawnTrain(BaseModel):
    """晨曦号列车"""
    userId = models.CharField(max_length=50, default='')
    inputDate = models.DateTimeField(auto_now_add=True)
    stationA= models.TextField(null=False, default='')
    stationB= models.TextField(null=False, default='')
    stationC= models.TextField(null=False, default='')
    stationD= models.TextField(null=False, default='')
    stationE= models.TextField(null=False, default='')
    stationF= models.TextField(null=False, default='')
    stationG= models.TextField(null=False, default='')
    wechatId= models.TextField(null=False, default='')
    sawUserId=models.TextField(null=False, default='')

