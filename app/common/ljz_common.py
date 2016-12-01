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
    """在path路径下，创建name文件

    return: (result, filepath)  
    result： True／False
    """
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
    """保存上传的文件

    1. 解析上传文件的 来源（name），md5值（file_md5），后缀（ext） 
    2. 拼接文件名和路径：file_md5 + '.' + ex，创建路径并保存
    3. 校验md5值
    """
    logger.debug('i am save_ordersource......')
    name = request.forms.name #订单来源名称
    file_md5=request.forms.testmd5
    data = request.files.data
    ext  = data.filename.split('.')[-1] #上传文件后缀
    save_name = file_md5 + '.' + ext

    state,filepath = mkdir(ordersource_path(), name)

    if state:
        new_file=os.sep.join([filepath,save_name])
        if not os.path.exists(new_file):
            data.filename=save_name
            logger.debug(data.filename)
            data.save(filepath, overwrite=True)
            if cal_md5(new_file)==file_md5:
                return '上传成功'
            else:
                os.remove(new_file)
                return '上传失败,请重新上传'
        else:
            return '文件已存在，请勿重复上传'
    else:
        return filepath

# setting.tpl
# users: 'account1#passwd1#name1,account2#passwd#name2'
setting_info = {
    'username':'Test',
    
    'account':'请输入账号', 'password':'请输入密码', 'backuptime':'00:00','intval':'',

    'users':''
}

def init_setting_html():
    try:
        system_query = System.select()
        admin_query = Admin.select()
    except BaseException,e:
        logger.error(e)
        return e
    user_str=''
    if (len(system_query) == 1):
        setting_info['account'] = system_query[0].username
        setting_info['password'] = system_query[0].passwd
        setting_info['backuptime'] = str(system_query[0].backuptime)[0:-3]
        setting_info['intval'] = str(system_query[0].intval)
    if (len(admin_query) >= 1):
        for item in admin_query:
            if not item.is_admin:
                user_str += str(item.id)
                user_str += '#'
                user_str += item.user 
                user_str += '#'
                user_str += item.passwd
                user_str += '#'
                user_str += item.name
                user_str += ','
        user_str = user_str[0:-1]
        setting_info['users'] = user_str 
    return setting_info


def yunpan():
    yaccount  = bottle.request.forms.get('username').decode('utf-8')
    ypassword = bottle.request.forms.get('passwd').decode('utf-8')
    ytime     = bottle.request.forms.get('backuptime')+':00'
    try:
        if (len(System.select()) == 1): #已有账号，进行更改
            System.update(username=yaccount, passwd=ypassword, backuptime=ytime).where(System.id==1).execute()
        else: # 初始化账号
            System.insert(id=1, username=yaccount, passwd=ypassword, backuptime=ytime).execute()
        return 'success'
    except BaseException,e:
        logger.error(e)
        return 'error'


def adduser():
    user_id=bottle.request.forms.get('id').decode('utf-8')
    user = bottle.request.forms.get('user').decode('utf-8')
    passwd = bottle.request.forms.get('passwd').decode('utf-8')
    name = bottle.request.forms.get('name').decode('utf-8')
    try:
        Admin.insert(id=user_id, user=user, name=name,passwd=passwd,is_admin=0,enable=1).execute()
        return 'success'
    except BaseException,e:
        logger.error(e)
        return 'error'


def deluser():
    user_id=bottle.request.forms.get('id')
    try:
        Admin.delete().where(Admin.id==user_id).execute()
        return 'success'
    except BaseException,e:
        logger.error(e)
        return 'error'
