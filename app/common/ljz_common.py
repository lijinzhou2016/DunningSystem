#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : config.py
# Author        : Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : support base conf
#*****************************************************************************
import sys,os  
from hashlib import md5


# 当前绝对路径
def get_path(name, parent=False, root=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    if root:
        path_comp.pop()
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')

def resource_path():
    return get_path('resource',parent=True)

def uploadfiles_path():
    return os.sep.join([resource_path(),'uploadfiles'])

def ordersource_path():
    return os.sep.join([uploadfiles_path(), 'ordersource'])

execfile(common_path()+os.sep+'db.py')
execfile(common_path()+os.sep+'mylogger.py')
logger = log('ljz_common.py')

def mkdir(path, name):
    filepath = os.sep.join([path, name])
    try:
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        return (True,filepath)
    except BaseException,e:
        logger.error(e)
        return (False,e)

def cal_md5(name):
    m = md5()
    a_file = open(name, 'rb')    #需要使用二进制格式读取文件内容
    m.update(a_file.read())
    a_file.close()
    logger.debug(m.hexdigest())
    return m.hexdigest()
    

def save_ordersource():
    logger.debug('i am save_ordersource......')
    name = request.forms.name #订单来源名称
    file_md5=request.forms.testmd5
    data = request.files.data
    ext  = data.filename.split('.')[-1] #上传文件后缀
    save_name = file_md5 + '.' + ext

    state,filepath = mkdir(ordersource_path(), name)

    if state:
        if not os.path.exists(os.sep.join([filepath,save_name])):
            data.filename=save_name
            logger.debug(data.filename)
            data.save(filepath, overwrite=True)
            if cal_md5(os.sep.join([filepath,save_name]))==file_md5:
                return '上传成功'
            else:
                return '上传失败'
        else:
            return '文件已存在，请勿重复上传'
    else:
        return filepath