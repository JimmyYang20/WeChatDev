# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseServerError,JsonResponse
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import (TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, EventMessage, ShortVideoMessage)
from mainapp import models as main_models
import random
import logging


# 开发配置
token='voaxioamiquan'
appid='wx55323c41e986dbdb'
appsecret='db38ee35dcfb7ef4f5ffe1c684fbd3c0'
encrypt_mode='nomal'
encoding_aes_key='5dK6MCUQ8whm44rrNk26HpFGxjdBJ2UBttNCXGbDPgH'


# 测试配置
# token='voaxioamiquan'
# appid='wx9a703578b0e7cbfd'
# appsecret='ec84a3ee9f3bff811eca71e95e0a609c'
# encrypt_mode='nomal'



conf = WechatConf(
    token=token,
    appid=appid,
    appsecret=appsecret,
    encrypt_mode=encrypt_mode,
    encoding_aes_key=encoding_aes_key
)

station = ['失望', '痛苦', '分裂', '自省', '领悟', '觉醒', '重生', '晨曦', '微信号']
infoDict = dict.fromkeys(station,"")

@csrf_exempt
def wechat_home(request):
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    wechat_instance = WechatBasic(conf=conf)
    if not wechat_instance.check_signature(signature,timestamp,nonce):
        return HttpResponseBadRequest('Verify Failed')
    else:
        if request.method == 'GET':
            res = request.GET.get('echostr', 'error')
            return HttpResponse(res, content_type='application/xml')
        else:
            try:
                wechat_instance.parse_data(request.body)
                message = wechat_instance.get_message()
                res = dawn_train(message,wechat_instance)
            except ParseError:
                return HttpResponseBadRequest('Invalid XML Data')
            return HttpResponse(res, content_type='application/xml')

def dawn_train(message,instance):
    if isinstance(message,EventMessage):
        eventType=message.type
        if isinstance(eventType,basestring):
            eventType = eventType.decode('utf8')
        if eventType == 'subscribe':
            reply_text = '真好，你没有错过我！\n\n相见就是缘分，我为你准备了见面礼。\n\n' \
                         '点击拿英语资源：<a href="https://mp.weixin.qq.com/s?__biz=MzU3OTIzNDEzNQ==&mid=100001405&idx=1&sn=a1014842ae9b05b4d8ff95e55b5bab6c&scene=19#wechat_redirect">英语资源</a>\n\n' \
                         '点击看往期文章：<a href="http://mp.weixin.qq.com/mp/homepage?__biz=MzU3OTIzNDEzNQ==&hid=3&sn=fe983c4aff32025ba9035f2b1da7650b#wechat_redirect">往期文章汇总</a>\n\n' \
                         '为了更好的相互了解，我会不定期发起圈内活动！\n' \
                         '点击查看目前进行中的活动：\n<a href="https://mp.weixin.qq.com/s?__biz=MzU3OTIzNDEzNQ==&mid=2247488156&idx=1&sn=1171399d2a0548a81b1c52525d5d8cca&chksm=fd6862a4ca1febb26195d031b93bd3cfde303f54b992d0492ccd2930b6d16a86cd9fafd58675#rd">2017，Fuckyou！我要回家！</a>\n\n感谢相遇。祝好：）'
            res = instance.response_text(reply_text)
            return res
        else:
            pass
    elif isinstance(message,TextMessage):
        keywords = ['长难句', '英语基础','新概念','四六级','听力','词汇','口语','语法','考研']
        userId = message.source
        content = message.content
        if isinstance(content,basestring):
            content = content.decode('utf8')
        stationLabel = content[0:2]
        if content in str(range(0,8)):
            content = int(content)
            if content == 0:
                onStation = station[content]
                reply_text = '尊敬的乘客，列车已达' + onStation + '站！\n' \
                            '欢迎您留言！\n' \
                            '主题：'+onStation+'\n' \
                            '请回复:\n' \
                             + onStation + '站留言：您的留言\n（注意：要写...留言：）'

                res = instance.response_text(reply_text)
                return res
            elif (content in range(1,7)) & (infoDict[station[content-1]] != ""):
                onStation = station[content]
                reply_text = '尊敬的乘客，列车已达' + onStation + '站!\n' \
                        '欢迎您留言!\n' \
                        '主题：'+onStation+'\n' \
                         '请回复:\n' + onStation + '站留言：您的留言\n（注意：要写...留言：）'
                res = instance.response_text(reply_text)
                return res
            elif (content == 7) & (infoDict[station[content-1]] != ""):
                onStation = station[content]
                reply_text = '尊敬的乘客，列车已达终点站' + onStation + '站，感谢您的的陪伴！，' \
                            '提前祝您新年快乐！\n，欢迎您的留下微信号!\n请回复:\n微信号：您的微信号\n（注意：要写...留言：）'
                res = instance.response_text(reply_text)
                return res
            else:
                reply_text = '您没有按活动提示进行操作，请按活动提示进行操作！'
                res = instance.response_text(reply_text)
                return res
        elif content == '出发':
            objList = main_models.DawnTrain.objects.filter(userId = userId)
            if len(objList) == 0:
                reply_text = '尊敬的乘客，欢迎乘坐晨曦号，本次列车即将出发，前往终点站晨曦站！\n启动列车，请回复:【0】'
                res = instance.response_text(reply_text)
                return res
            else:
                reply_text = '尊敬的乘客，你已经完成了旅行！'
                res = instance.response_text(reply_text)
                return res
        elif '微信号' in content:
            infoDict[station[7]] = content
            reply_text = '恭喜你完成了旅程！您可以在“列车留言录"里查看是其他人的留言，请回复:查看'
            try:
                obj = main_models.DawnTrain(
                    userId = userId,
                    stationA=infoDict[station[0]],
                    stationB=infoDict[station[1]],
                    stationC=infoDict[station[2]],
                    stationD=infoDict[station[3]],
                    stationE=infoDict[station[4]],
                    stationF=infoDict[station[5]],
                    stationG=infoDict[station[6]],
                    wechatId=infoDict[station[7]],
                )
                obj.save()
            except:
                print '数据存储错误'
                return HttpResponseBadRequest('数据存储错误！')
            res = instance.response_text(reply_text)
            return res
        elif content == '查看':
            userlist = main_models.DawnTrain.objects.filter(userId=userId)
            if len(userlist) != 0:
                user = userlist[0]
                sawUserId = user.sawUserId
                userIds = sawUserId.split(' ')
                print userIds
                if len(userIds) <= 3:
                    userIds.append(userId)
                    objlist = main_models.DawnTrain.objects.exclude(userId__in=userIds)
                    if len(objlist) != 0:
                        obj = random.sample(objlist, 1)[0]
                        sawUserId = sawUserId + ' ' + obj.userId
                        user.sawUserId = sawUserId
                        user.save()
                        reply_text = obj.stationA + '\n' + \
                                     obj.stationB + '\n' + \
                                     obj.stationC + '\n' + \
                                     obj.stationD + '\n' + \
                                     obj.stationE + '\n' + \
                                     obj.stationF + '\n' + \
                                     obj.stationG + '\n' + \
                                     obj.wechatId + '\n' + \
                                     '如果您想继续查看留言，\n' \
                                     '请回复:查看'
                        res = instance.response_text(reply_text)
                        return res
                    else:
                        reply_text = '你已经看完所有乘客的留言了，请等待其他乘客上车后再查看！'
                        res = instance.response_text(reply_text)
                        return res
                else:
                    reply_text = '尊敬的乘客，您已经看了三位乘客的留言了！\n' \
                                 '快回家吧，注意安全！\n' \
                                 '新年快乐哦！'
                    res = instance.response_text(reply_text)
                    return res
            else:
                reply_text = '尊敬的乘客，你还没有到终点站，不能查看终点站的留言！'
                res = instance.response_text(reply_text)
                return res
        elif stationLabel in station:
            infoDict[stationLabel] = content
            nextStation = station.index(stationLabel) + 1
            reply_text = ''
            if nextStation <= 7:
                reply_text = '尊敬的乘客，我们已经帮你记录下' + station[nextStation - 1] + '站的足迹，继续您的旅程，请回复:【' + str(nextStation) + '】\n'
            res = instance.response_text(reply_text)
            return res
        elif content in keywords:
            obj = main_models.KeywordReply.objects.get(keyword=content)
            reply_text = obj.content
            res = instance.response_text(reply_text)
            return  res
        else:
            reply_text = '您没有按活动提示进行操作，请按活动提示进行操作！'
            res = instance.response_text(reply_text)
            return res
    else:
        reply_text = '此类型消息还在开发中！'
        res = instance.response_text(reply_text)
        return res
