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
import bottle

from common.db import System, Admin
from common.mylogger import log


def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')


logger = log('setting.py')

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
        logger.error(str(e))
        return str(e)
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
                user_str += '#'
                user_str += str(item.enable)
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
        logger.error(str(e))
        return 'error'


def deluser():
    user_id=bottle.request.forms.get('id')
    try:
        Admin.update(enable=0).where(Admin.id==user_id).execute()
        return 'success'
    except BaseException,e:
        logger.error(str(e))
        return 'error'
