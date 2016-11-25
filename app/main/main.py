#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : main.py
# Author        : chxs&Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : server api
#*****************************************************************************

import bottle
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

execfile(os.path.dirname(os.path.abspath(__file__))+os.sep+'util.py')

# load .tpl dir
bottle.TEMPLATE_PATH.append(www_path())
# create log obj
logger = log('main.py')

logger.debug('dunning server start')

@bottle.error(404)
def error404():
    return bottle.static_file('404.html', root=www_path())

# 静态信息文件 127.0.0.1:8080/
@bottle.route('/:filepath')
def server_www(filepath):
    file_name, file_type = os.path.splitext(filepath)
    if file_name == 'index':
        return bottle.static_file('index.html', root=www_path())
    elif file_type == '.html':
        return bottle.static_file(filename, root=www_path())
    elif file_type == '.css':
        return bottle.static_file(filepath, root=css_path())
    elif file_type == '.js':
        return bottle.static_file(filepath, root=js_path())
    elif file_type in ['.png','.PNG','.jpg','.JPG','.gif']:
        return bottle.static_file(filepath, root=images_path())

@bottle.route('/login', method='POST')
def login():
    logger.debug('i am login')
    name = bottle.request.forms.get('username')
    passwd = bottle.request.forms.get('password')
    logger.debug(name)
    userinfo = Userinfo.check_login(name, passwd)
    if not userinfo:
        return {'result':'error'}
    else:
        return get_userinfo_dic(userinfo)

@bottle.route('/orderlist')
@bottle.view('orderlist')
def orderlist():
    page_index = bottle.request.query.pageIndex
    logger.debug(page_index)

    # util.py 中定义
    return order_list_info

@bottle.route('/order/detail')
def orderdetail():
    pass 


@bottle.route('/setting')
@bottle.view('setting')
def setting():
    logger.debug('i am setting')
    action = bottle.request.forms.get('action') #post
    if not action:
        action = bottle.request.query.action #get
    logger.debug(action)
    if action == 'yunpan':
        """ 网盘账号设置 """
        yaccount  = bottle.request.query.get('username')
        ypassword = bottle.request.query.get('passwd')
        ytime     = bottle.request.query.get('backuptime')+':00'
        if (len(System.select()) == 1):
            # 更新网盘
            sql_update = 'update system set username="{0}", passwd="{1}", backuptime="{2}" where id=1;'.format(yaccount, ypassword, ytime)
            op_sql(sql_update)
        else: #插入
            sql_insert = 'insert system values (1, "{0}", "{1}", "{2}", 1)'.format(yaccount, ypassword, ytime)
            op_sql(sql_insert)

    elif action == 'adduser':
        """ 添加管理员 """
        logger.debug('start add user.......')

        user_id=bottle.request.query.get('id')
        user = bottle.request.query.get('user')
        passwd = bottle.request.query.get('passwd')
        name = bottle.request.query.get('name').decode('utf-8')

        sql_adduser = 'insert admin values ({0}, "{1}", "{2}", "{3}", 0, 1)'.format(user_id, user, name, passwd)
        return op_sql(sql_adduser)

    elif action == 'deluser':
        """ 删除管理员 """
        user_id=bottle.request.query.get('id')
        sql_deluser = 'delete from admin where id="{0}"'.format(user_id)
        return op_sql(sql_deluser)

    elif action == 'jump':
        """ 加载设置页面 """
        try:
            system_query = System.select()
            admin_query = Admin.select()
        except BaseException,e:
            logger.error(e)
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
        logger.debug(setting_info)
        return setting_info


    else:
        logger.debug('unknown')

#用户信息封装成json返回
def get_userinfo_dic(userinfo):
    return dict(zip(['result','name','passwd','is_admin'],['success',userinfo.name, userinfo.passwd, userinfo.is_admin]))

def op_sql(sql_cmd):
    try:
        logger.debug(sql_cmd)
        database.execute_sql(sql_cmd)
        result={'state':'success'}
        logger.debug(result['state'])
    except BaseException,e:
        logger.error(e)
        result = {'state':e}
    finally:
        return result

bottle.run(host='127.0.0.1', port='8080', debug=False)

