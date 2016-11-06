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
import ConfigParser  
import logging

###################

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
# 记录一条日志
logger.info('foorbar')



####################

class Config(object):  
  def __init__(self, config_file_path):  
    cf = ConfigParser.ConfigParser()  
    cf.read(config_file_path)  
  
    s = cf.sections()  
    print 'section:', s  
  
    # o = cf.options("db")  
    # print 'options:', o  
  
    # v = cf.items("server")  
    # print 'db:', v  
  
    # db_host = cf.get("db", "host")  
    # db_port = cf.getint("db", "port")  
    # db_user = cf.get("db", "user")  
    # db_pwd = cf.get("baseconf", "password")  
  
    # print db_host, db_port, db_user, db_pwd  
  
    # cf.set("baseconf", "db_pass", "123456")  
    # cf.write(open("config_file_path", "w")) 


if __name__ == "__main__":  
  f = Config(r"C:\Users\lijinzhou\Desktop\DunningSystem\config\conf.ini")  

