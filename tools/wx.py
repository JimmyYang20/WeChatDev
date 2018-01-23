# -*- coding: utf-8 -*-
import requests
import json
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def request_session(url):
    '''
    该函数只适合ssl单向认证
    :return: dict
    '''
    #url = "https://passport.cnblogs.com/user/signin"
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0" }
    r = requests.get(url, headers=headers, verify=False)
    #return r.json
    return json.loads(r.text)

def get_session(url=None, **param):
    '''
    调用request_session函数到微信服务器取session_key
    https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=secret&jscode=jscode&grant_type=authorization_code
    '''
    params = []
    for k,v in param.iteritems():
        params.append('{}={}'.format(k,v))
    param_str = '&'.join(params)
    if url==None:
        url = 'https://api.weixin.qq.com/sns/jscode2session'
    wx_session_url = '%s?%s'%(url,param_str)
    return request_session(wx_session_url)
