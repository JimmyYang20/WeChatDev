# -*- coding: utf-8 -*-
import json
class BaseError():
    def __init__(self, message=None):
        self.__dict__.update({'success': False, 'message':message})

    def toDict(self):
        return self.__dict__

    '''
    def __str__(self):
        str = []
        for k,v in self.__dict__.iteritems():
            str.append('{}:{}'.format(k,v))
        return '{' + ','.join(str) + '}'
    '''
    def __str__(self):
        return json.dumps(self.__dict__,ensure_ascii=False)

class CartViewError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'CT002', 'errMsg': '查看购物车发生异常'})

class CartError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'CT001', 'errMsg': '添加购物车处理异常'})
class CartDelError(BaseError):
    def __init__(self, message=None):
        BaseError.__init__(self, message)
        sefl.__dict__.update({'errorCode':'CT003', 'errMsg': '删除购物车发生异常'})

class CartJsonError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'CT003', 'errMsg': '购物车数据转换发生异常'})

class BillAddError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'B0001', 'errMsg': '订单处理发生异常'})

class BillStatusError(BaseError):
    def __init__(self, message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'B0002', 'errMsg': '订单状态处理发生异常'})

class ConnError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'C0001', 'errMsg': '链接参数错误'})

class ContactModError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'CM001', 'errMsg': '更新联系方式发生异常'})

class SessionError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'S0001', 'errMsg': '获取微信服务器权限失败'})

class AuthError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'A0001', 'errMsg': '未授权的操作'})

class LoginError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'L0001', 'errMsg': '系统登录发生异常'})

class DbError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'DB001', 'errMsg': '数据库存储错误'})

class UserError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'U0001', 'errMsg': '用户数据处理异常'})

class FileError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'F0001', 'errMsg': '保存图像文件发生异常'})

class NoProductError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'PD001', 'errMsg': '必须上传产品主图'})

class AddressListError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'CT001', 'errMsg': '获取收货人地址发生异常'})

class ProductNotEnoughError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'PN001', 'errMsg': '商品库存不足'})

class ParamError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode': 'P0001', 'errMsg': '业务参数错误'})

class CommentAddError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode': 'CM001', 'errMsg': '评论数据模型错误'})


        self.__dict__.update({'errCode':'U0001', 'errMsg': '用户模型异常'})

class DoctorError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'U0001', 'errMsg': '医生数据异常'})

class AnswerError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'A0001', 'errMsg': '答案数据异常'})

class ConfirmNoticeError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'CN001', 'errMsg': '告知书数据异常'})

class NaireError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'N0001', 'errMsg': '调查问卷数据异常'})

class IdentityError(BaseError):
    def __init__(self,message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'I0001', 'errMsg': '用户身份申请异常'})

class DiseaseError(BaseError):
    def __init__(self, message=None):
        BaseError.__init__(self, message)
        self.__dict__.update({'errCode': 'D0001', 'errMsg': '慢病数据异常'})
class HealthInformationError(BaseError):
    def __init__(self, message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'I0001','errMsg': '医保资讯异常'})

class AIError(BaseError):
    def __init__(self, message=None):
        BaseError.__init__(self,message)
        self.__dict__.update({'errCode':'AI001','errMsg': 'AI服务器异常'})

