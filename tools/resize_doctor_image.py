#!/usr/bin/python
#-*- coding:utf-8-*-
from PIL import Image
import os
if __name__=='__main__':
    img_path = '/data/RawData/2017附院照片'
    small_path = '/data/RawData/doctorImages'
    imgs = os.listdir(img_path)
    for img in imgs:
        imgf = os.path.join(img_path,img)
        small_imgf = os.path.join(small_path, img)
        if os.path.exists(small_imgf):
            continue
        org_img = Image.open(imgf)
        try:
            small_img = org_img.resize((220,300), Image.BILINEAR)
        except Exception as e:
            print img
        small_img.save(small_imgf,'JPEG')

