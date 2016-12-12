#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : session.py
# Author        : chenxiaosuo
# Created       : 10th Nov 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : support session for user login
#*****************************************************************************

import time
import uuid
import os
from peewee import *

# 过期时间为300秒
session_expires = 3000
#存放所有用户的信息
user_list = {}

def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')


execfile(common_path() + os.sep + 'db.py')


#用户登录信息
class Session(object):
    def __init__(self):
        pass

    def __init__(self, name):
        self.name = name
        #过期时间
        self.expire_time = int(time.time()) + session_expires
        #根据时间戳和用户名计算出hash，保证唯一性
        self.session = name + '_' + str(uuid.uuid1(hash(name) % 2 ^ 48))
    
    #更新记录，刷新过期时间
    def __refresh(self):
        self.expire_time = int(time.time()) + session_expires
    
    #校验session是否正确，如正确，则刷新过期时间（说明客户端访问过一次）
    def validate(self, session_str):
        #首先判断是否超时
        if self.expire_time > int(time.time()):
            #再判断是否正确
            if self.session == session_str:
                #刷新时间
                self.__refresh()
                return True
            else:
                return False
        else:
            return False

#用户信息
class Userinfo:

    def __init__(self, user = '', name = '', passwd = '', is_admin = 0):
        self.id = 0
        self.user = user
        self.name = name
        self.passwd = passwd
        self.is_admin = is_admin
        self.session = Session(self.name)

    #根据session字段获取用户信息， 如果校验失败，则返回None   
    @classmethod
    def get_by_session(self,session_str):
        name = session_str.split('_')[0]
        #如果存在，则判断正确性
        if user_list.has_key(name):
            if user_list[name].session.validate(session_str):
                return user_list[name]
            else:
                return None
        else:
            return None
    
    #校验用户名和密码，生成用户信息，插入到user_list中
    @classmethod
    def check_login(self, user, passwd):
        query = (Admin.select().where((Admin.user == user) 
                & (Admin.passwd == passwd) & (Admin.enable == 1)))
        if(len(query) == 1):
            userinfo = Userinfo(user)
            userinfo.id = query[0].id
            userinfo.name = query[0].name
            userinfo.passwd = query[0].passwd
            userinfo.is_admin = query[0].is_admin
            userinfo.session = Session(userinfo.user)
            user_list[userinfo.user] = userinfo
            return userinfo
        else:
            return None

    #格式化用户信息，返回字典
    def dict_format(self):
        user_dict = { 'id': self.id, 'name': self.name, 'passwd': self.passwd,
                    'is_admin': self.is_admin, 'session': self.session.session,
                    'user': self.user}
        return user_dict