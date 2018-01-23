# -*- coding: utf-8 -*-
from django.utils.crypto import get_random_string
from django.core.serializers import serialize
import datetime
import string
import json
import os

__all__ = [
    'batch',
    'gen_random_filename',
    'save_cache_image',
]

VALID_KEY_CHARS = string.ascii_lowercase + string.digits

def batch(iterable, n=1):
    """
    分批返回iterable

    @param: iterable:可迭代的变量
    @param n(int): batch size
    @return: iterable: 一批可迭代的变量
    """
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def gen_random_filename(subfix):
    '''
    生成随机文件名

    @subfix: 后缀名，'.jpg', '.png'等等,如果输入的是'adfdfdf.jpg'会截取后缀名
    '''
    _subfix = os.path.splitext(subfix)
    if _subfix[1] == '':
        try:
            _tmp = _subfix[0].index('.')
            subfix = _subfix[0]
        except:
            subfix = '.jpg'
    else:
        if len(_subfix[1]):
            subfix = '.jpg'
        else:
            subfix = _subfix[1]

    datestr = str(datetime.datetime.now()).replace('-','').replace(':','').replace('.','').replace(' ','')
    filename = '{}-{}{}'.format(datestr,get_random_string(16, VALID_KEY_CHARS), subfix)
    return filename

def serialize_bootstraptable(queryset):
    '''
    django 到 bootstrap-table 的数据接口
    :param queryset: django queryset
    :return: json data
    '''
    json_data = serialize('json', queryset)
    json_final = {"total": queryset.count(), "rows": []}
    data = json.loads(json_data)
    for item in data:
        del item["model"]
        item["fields"].update({"id": item["pk"]})
        item = item["fields"]
        json_final['rows'].append(item)
    return json_final

def save_cache_image(imgdata,image_path='/sd/data/temp/furnisearch'):
    '''
    save image data to png file

    @param imgdata: 图像数据
    @param image_path(string): default '/sd/data/temp/furnisearch', 保存图像的目录
    @return: 图片绝对路径
    '''
    filename_ = str(datetime.datetime.now()).replace(' ', '_') + '_%d.jpg'%(np.random.randint(1000))
    #有时间可以从图像头文件中获取图像的格式，而不是指定jpg

    namef = os.path.join(image_path,filename_)
    with open(namef,'wb') as f:
        f.write(imgdata)
    return namef

