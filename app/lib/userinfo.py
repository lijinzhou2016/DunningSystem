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

# 过期时间为300秒
session_expires = 300


#用户登录信息
class session(object):
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



