#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : Orderinfo.py
# Author        : ljz
# Created       : 21th Nov 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : Get order info by order id
#*****************************************************************************

import time
import uuid
import os
import math
import datetime
from peewee import *
import xlrd
import re

def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1]=name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')

execfile(common_path() + os.sep + 'db.py')
execfile(common_path() + os.sep + 'config.py')
execfile(common_path() + os.sep + 'mylogger.py')
logger = log('orderlistinfo.py')

# 数据库表状态字段转换字符状态的对应列表
orderStatus = {0:'已结清', 1:'联系本人', 2:'联系亲属',3:'联系同学',
                4:'失联',5:'待外访',6:'外访中',7:'承诺还款',8:'部分还款'}

# 用来把前端传过来的状态，转换成数据库对应数值的列表
orderStatusKey = {u'已结清':0, u'联系本人':1, u'联系亲属':2,u'联系同学':3,
                u'失联':4,u'待外访':5,u'外访中':6,u'承诺还款':7,u'部分还款':8}

# 上传的Excel表格模板字段
order_file_title=[u'订单编号',u'姓名',u'电话',u'身份证',u'学校区域',u'学校',u'家庭区域',u'家庭住址',u'订单状态',
                    u'账期',u'产品名称',u'分期金额',u'首次还款日',u'月供',u'期数',u'已还期数',
                    u'订单日期',u'接单日期',u'已还金额',u'父母',u'父母电话',u'同寝',u'同寝电话',u'同学',u'同学电话']
# 搜索条件字典
search_item = {
        'order_username': '',
        'order_zhangqi': '',
        'order_school': '',
        'order_jtzz': '',
        'order_jtqy': '',
        'order_jdrq': '',
        'order_ddzt': '',
        'order_shxx': '',
        'school_area': ''
    }

statues_keys = ['已结清','联系本人', '联系亲属','联系同学','失联','待外访', '外访中', '承诺还款', '部分还款']
zhangaqi_keys= ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12']

class OrderList:
    def __init__(self, pageindex, userinfo, condition):
        self.pageindex = pageindex
        self.condition = int(condition)
        self.userinfo = userinfo    # 用户信息
        self.orders_return_info = {'userinfo':{},'fenyeinfo':{}, 'orders_list':[], 'condition':{}}   # 返回字典
        self.orders_one_info={'name':'','detailurl':'','ordernumber':'','phone':'','qiankuan':'','orderdata':'','acquiringdata':'','school':'','state':''}
        self.orders_return_info['userinfo']=self.userinfo
        if self.condition == 0: # 无搜索条件
            self.orders_count = Orders.select().where(Orders.is_del == 0).count()   # 订单总条数
            self.total_pages = 1 if self.orders_count==0 else int(math.ceil(self.orders_count/10.0))   # 分页数
            self.orders_return_info['condition'] = search_item
            self.orders_return_info['fenyeinfo']={
                'pageIndex'   : self.pageindex, 
                'total_pages' : self.total_pages, 
                'total_orders': self.orders_count, 
                'setting_url' : r'/setting?session='+self.userinfo['session'],
                'detail_url'  : r'/orderdetail/0?session='+self.userinfo['session'] # 空的详单页面链接
            }
        
            # 按请求索引查找相应数据
            if self.orders_count == 0:
                self.orders_list_info =[]
            else :
                query = Orders.select().where(Orders.is_del == 0).order_by(-Orders.create_time,-Orders.modify_time)
                if self.orders_count > int(pageindex)*10:
                    self.orders_list_info = query[(int(pageindex)-1)*10:int(pageindex)*10]
                else:
                    self.orders_list_info = query[(int(pageindex)-1)*10:]
        else: # condition == 1：有搜索条件的情况
            self.orders_count = 0
            self.total_pages = 0
            self.orders_list_info =[]
    
    def set_orders_data(self):
        if self.condition == 1: # 含有搜索条件
            self.condition_data()
        else: # 没有索索条件
            self.no_condition_data()

    @property
    def get_orders_data(self):
        return self.orders_return_info


    def condition_data(self):

        # 获取查询条件
        condition_item={
            'order_username': bottle.request.query.order_username,
            'order_zhangqi': bottle.request.query.order_zhangqi,
            'order_school': bottle.request.query.order_school,
            'order_jtzz': bottle.request.query.order_jtzz,
            'order_jtqy': bottle.request.query.order_jtqy,
            'order_jdrq': bottle.request.query.order_jdrq,
            'order_ddzt': bottle.request.query.order_ddzt,
            'order_shxx': bottle.request.query.order_shxx,
            'school_area': bottle.request.query.school_area
        }

        # debug
        for key in condition_item.keys():
            if condition_item[key]:
                logger.debug(key + " : " + condition_item[key])

 
        lender_id = [] # 存放lender表查询到的数据id
        lender_query = [] # 存放lender表查询到的数据对象
        lender_flag = 0 # 0: 无搜索条件 。1: 有搜索条件，但未查到数据
        orders_flag = 0
        temp_query=[] # 存放从仅从orders表中查询的数据列表，没有和lender表取交集

        orders_query = [] # 最终查到的数据

        # 如果lender表有搜索字段，则查询lender表
        if len(condition_item['order_jtzz'] + condition_item['order_username'] + condition_item['order_school'] + condition_item['order_jtqy'] + condition_item['school_area'])>0:
            logger.debug('select lender ... ')
            lender_query = Lender.select().where(   
                Lender.name.contains(condition_item['order_username']),
                Lender.university.contains(condition_item['order_school']),
                Lender.family_addr.contains(condition_item['order_jtzz']),
                Lender.family_area.contains(condition_item['order_jtqy']),
                Lender.univers_area.contains(condition_item['school_area'])
            )

            # 按条件查询到的数据，取出id添加到lender_id
            if len(lender_query)>=1: 
                logger.debug("find data in lender") 
                for lender in lender_query:
                    if lender.is_del == 0:
                        lender_id.append(lender.id)
            else: 
                lender_flag = 1 # 表示按照搜索条件没有查询到数据
            logger.debug('lender id : '+str(len(lender_id)))

        if condition_item['order_zhangqi']: # 账期搜索
            account_day_query = Orders.select().where((Orders.account_day == condition_item['order_zhangqi']) & (Orders.is_del == 0)).order_by(-Orders.create_time, -Orders.modify_time)
            if len(account_day_query)>0:
                temp_query.append(account_day_query)
            else:
                orders_flag = 1 
        if condition_item['order_shxx']: # 接单日期搜索
            logger.debug('查询接单日期字段：'+condition_item['order_shxx'])
            takeorder_data_query = Orders.select().where((Orders.takeorder_data == condition_item['order_shxx']) & (Orders.is_del == 0)).order_by(-Orders.create_time, -Orders.modify_time)
            logger.debug(len(takeorder_data_query))
            if len(takeorder_data_query)>0:
                temp_query.append(takeorder_data_query)
            else:
                logger.debug('按接单字段查无数据')
                orders_flag = 1
        if condition_item['order_ddzt']: # 订单状态搜索
            logger.debug('开始查询订单状态')
            status_query = Orders.select().where((Orders.status == orderStatusKey[condition_item['order_ddzt']]) & (Orders.is_del == 0)).order_by(-Orders.create_time, -Orders.modify_time)
            if len(status_query)>0:
                temp_query.append(status_query)
            else:
                orders_flag = 1
        if condition_item['order_jdrq']: # 订单日期搜索
            order_date_query = Orders.select().where((Orders.order_date == condition_item['order_jdrq']) & (Orders.is_del == 0)).order_by(-Orders.create_time, -Orders.modify_time)
            if len(order_date_query)>0:
                temp_query.append(order_date_query)
            else:
                orders_flag = 1
        
        logger.debug(len(temp_query))
        if len(temp_query)>0: # 在orders表中查询到数据
            # 取交集
            orders_query = list(set(temp_query[0]).intersection(*temp_query[1:]))

            if len(orders_query)==0: # 若无交集，说明搜索条件有冲突，无数据
                logger.debug('说明搜索条件有冲突，无数据')
                orders_flag = 1

        
        if lender_flag == 1 or orders_flag == 1: # 说明查询条件有冲突，没有查到数据
            self.orders_return_info['orders_list'].append(self.orders_one_info)

        elif len(orders_query)>0 and len(lender_id)>0: # 两个表均有查到数据
            logger.debug('lender orders中查到数据')
            for id_tmp in lender_id: # 依次取出lender表中搜索到的记录id
                for query_tmp in orders_query: # 取出orders表中搜索到的记录
                    if query_tmp.lender_id == id_tmp: # 若id相等，则保存
                        self.orders_list_info.append(query_tmp) # 搜索的最终数据 ！！！

        elif len(orders_query)>0: # orders 表中查到数据
            logger.debug('orders中查到数据')
            self.orders_list_info = orders_query # 搜索的最终数据 ！！！

        else: # lender表中查到数据
            logger.debug('lender中查到数据')
            self.orders_list_info = Orders.select().where((Orders.lender_id << lender_id) & (Orders.is_del == 0)).order_by(-Orders.create_time, -Orders.modify_time) # 搜索的最终数据 ！！！
            
        self.orders_count = len(self.orders_list_info)
        self.total_pages =  1 if self.orders_count==0 else int(math.ceil(self.orders_count/10.0)) # 分页数
        self.orders_return_info['fenyeinfo']={
            'pageIndex'   : self.pageindex, 
            'total_pages' : self.total_pages, 
            'total_orders': self.orders_count, 
            'setting_url' : r'/setting?session='+self.userinfo['session'],
            'detail_url'  : r'/orderdetail/0?session='+self.userinfo['session'] #
        }

        self.orders_return_info['condition'] = condition_item
        if len(self.orders_list_info):
            if self.orders_count > int(self.pageindex)*10:
                self.orders_list_info = self.orders_list_info[(int(self.pageindex)-1)*10:int(self.pageindex)*10]
            else:
                self.orders_list_info = self.orders_list_info[(int(self.pageindex)-1)*10:]
            self.no_condition_data()
        

    def no_condition_data(self):
        '''初始化返回字典的值

        '''
        for order_info_tmp in self.orders_list_info:
            lender_query=Lender.select().join(Orders).where(Orders.lender==order_info_tmp.lender).get()
            logger.debug(lender_query.name)

            def get_state():
                try:
                    state = orderStatus[order_info_tmp.status]
                    if state:
                        return state
                    else:
                        return "NULL"
                except BaseException as e:
                    logger.info(str(e))
                    return "NULL"
            # 计算总欠款
            def total_debt():
                try:
                    month_pay = float(order_info_tmp.month_pay) # 月供 0.00
                    periods = int(order_info_tmp.periods) # 期数  0
                    paid_periods = int(order_info_tmp.paid_periods) # 已还期数  0
                    amount = float(order_info_tmp.amount) # 分期金额  0.00
                    payment_day = order_info_tmp.payment_day # 首次还款日   ''
                except BaseException as e:
                    logger.info(str(e))
                    return "ERROR"

                # 缺少字段，无法计算
                if (month_pay == 0) or (periods == 0) or (amount == 0) or (payment_day == ''):
                    logger.error("ERROR: 缺少字段无法计算，请检查订单 {0} {1}".format(lender_query.name, order_info_tmp.disp))
                    return "NULL"
                
                if get_state() == "已结清" or periods==paid_periods:
                    logger.info("已结清订单: {0} {1}".format(lender_query.name, order_info_tmp.disp))
                    return 0.0

                # 计算逾期天数的起始日期：
                today = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
                over_day_list=[]
                payment_day_list = payment_day.split('-') # 格式如： ['2016', '12', '10']
             
                if int(payment_day_list[1]) + int(paid_periods) > 48:
                    payment_day_list[0] = str(int(payment_day_list[0])+4)
                    payment_day_list[1] = str(int(payment_day_list[1])+int(paid_periods)-48)
                elif int(payment_day_list[1]) + int(paid_periods) > 36:
                    payment_day_list[0] = str(int(payment_day_list[0])+3)
                    payment_day_list[1] = str(int(payment_day_list[1])+int(paid_periods)-36)
                elif int(payment_day_list[1]) + int(paid_periods) > 24:
                    payment_day_list[0] = str(int(payment_day_list[0])+2)
                    payment_day_list[1] = str(int(payment_day_list[1])+int(paid_periods)-24) 
                elif int(payment_day_list[1]) + int(paid_periods) > 12:
                    payment_day_list[0] = str(int(payment_day_list[0])+1)
                    payment_day_list[1] = str(int(payment_day_list[1])+int(paid_periods)-12)
                else:
                    payment_day_list[1] = str(int(payment_day_list[1])+int(paid_periods))
                
                if int(payment_day_list[0])>int(datetime.datetime.now().year):
                    logger.error("ERROR:请检查订单 {0} {1} 已还期数的数据".format(lender_query.name, order_info_tmp.disp))
                    return "NULL"
                elif int(payment_day_list[0])==int(datetime.datetime.now().year) and int(payment_day_list[1])>int(datetime.datetime.now().month):
                    logger.error("ERROR:请检查订单 {0} {1} 已还期数的数据".format(lender_query.name, order_info_tmp.disp))
                    return "NULL"

                year = int(payment_day_list[0])
                flag = True
                if (year % 4) == 0:
                    if (year % 100) == 0:
                        if (year % 400) == 0:
                            flag = True   # 整百年能被400整除的是闰年
                        else:
                            flag = False
                    else:
                        flag = True       # 非整百年能被4整除的为闰年
                else:
                    flag = False

                if int(payment_day_list[1])==2 and int(payment_day_list[2])>28:
                    if flag:
                        laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),29)
                    else:
                        laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),28)
                elif int(payment_day_list[1]) in [4,6,9,11] and int(payment_day_list[2])>30:
                    laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),30)
                else:
                    laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),int(payment_day_list[2]))
                over_day_list.append((today - laste_day).days) #逾期天数


                while True:
                    if int(payment_day_list[1]) + 1 > 12:
                        payment_day_list[0] = str(int(payment_day_list[0])+1)
                        payment_day_list[1] = str(int(payment_day_list[1])-12)
                    payment_day_list[1] = str(int(payment_day_list[1])+1)
                    logger.debug(str(payment_day_list))

                    # 已还期数超过当前日期的错误处理
                    if int(payment_day_list[0])>int(datetime.datetime.now().year):
                        logger.error("ERROR:请检查订单 {0} {1} 已还期数的数据".format(lender_query.name, order_info_tmp.disp))
                        return "NULL"
                    elif int(payment_day_list[0])==int(datetime.datetime.now().year) and int(payment_day_list[1])>int(datetime.datetime.now().month):
                        logger.error("ERROR:请检查订单 {0} {1} 已还期数的数据".format(lender_query.name, order_info_tmp.disp))
                        return "NULL"

                    if int(payment_day_list[0]) == int(datetime.datetime.now().year) and int(payment_day_list[1]) == int(datetime.datetime.now().month):
                        if int(payment_day_list[2]) > int(datetime.datetime.now().day):
                            break
                        else:
                            laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),int(payment_day_list[2]))
                            over_day_list.append((today - laste_day).days) #逾期天数
                            break

                    year = int(payment_day_list[0])
                    flag = True
                    if (year % 4) == 0:
                        if (year % 100) == 0:
                            if (year % 400) == 0:
                                flag = True   # 整百年能被400整除的是闰年
                            else:
                                flag = False
                        else:
                            flag = True       # 非整百年能被4整除的为闰年
                    else:
                        flag = False

                    if int(payment_day_list[1])==2 and int(payment_day_list[2])>28:
                        if flag:
                            laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),29)
                        else:
                            laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),28)
                    elif int(payment_day_list[1]) in [4,6,9,11] and int(payment_day_list[2])>30:
                        laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),30)
                    else:
                        
                        laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),int(payment_day_list[2]))
                    # 逾期时间超过期数
                    if len(over_day_list)+paid_periods >= periods:
                        break
                    over_day_list.append((today - laste_day).days) #逾期天数

                # 计算滞纳金
                
                total_late_fee = 0.0
                for over_day in over_day_list:
                    if over_day > 0:
                        if over_day >90:
                            late_fee = (month_pay*0.26/30.0)*90+(month_pay*0.50/30.0)*(over_day-90)
                        else:
                            late_fee = (month_pay*0.26/30.0)*over_day
                        logger.debug("over_day: {0}  over_money: {1}".format(over_day, late_fee))
                    else:
                        late_fee = 0.0
                    total_late_fee = total_late_fee + late_fee
                
                # 总欠款
                debt = month_pay*(periods - paid_periods)+total_late_fee
                logger.debug("{0}: 滞纳金 :{1}  总欠款：{2}".format(lender_query.name, total_late_fee, round(debt, 2)))
                logger.debug("========================================================")
                return round(debt, 2) #保留两位小数

            self.orders_return_info['orders_list'].append({
                'name' : lender_query.name,
                'detailurl' : r'/orderdetail/'+ str(order_info_tmp.id) + r'?session=' + self.userinfo['session'],
                'ordernumber' : order_info_tmp.disp,
                'phone' : lender_query.tel,
                'qiankuan' : total_debt(), # 需要计算
                'orderdata' : order_info_tmp.order_date if order_info_tmp.order_date else "NULL",
                'acquiringdata' : order_info_tmp.takeorder_data if order_info_tmp.takeorder_data  else "NULL",
                'school' : lender_query.university if lender_query.university  else "NULL",
                'state' : get_state()
            })

        # 不足10条数据，补空，满足前端显示一致
        for i in range(10 - len(self.orders_list_info)):
            self.orders_return_info['orders_list'].append(self.orders_one_info)


    # 解析上传的订单文件
    @staticmethod
    def save_orders_to_database(filepath, wherefrom):
        total_datas=[] # 总条数
        exception_disp='' # 异常订单
        order_insert_dict = {'is_del':0, 'source':wherefrom} # 插入order表的一条记录字典
        lender_insert_dict = {'is_del':0} # 插入lender表中的一条记录字典
        success_insert_count = 0

        try:
            data = xlrd.open_workbook(filepath)
            table = data.sheets()[0]
            nrows = table.nrows # 行数
        except BaseException,e:
            logger.error('打开文件出错: ')
            logger.error(str(e))
            os.remove(filepath)
            return '打开文件出错，请重新上传'

        for i in range(nrows): #着行读取文件数据
            total_datas.append(table.row_values(i))
        title = total_datas.pop(0) # 去掉标题栏
        # for i in title:
        #     logger.debug(i)
        for i in range(25):
            if not title[i] == order_file_title[i]:
                os.remove(filepath)
                return '文件模版错误，请核对后重新上传'

        for one_data in total_datas:
            # logger.debug(one_data)
            pattern =r'^\d{4}-\d{1,2}-\d{1,2}$' #匹配日期格式例如：2017-01-11
            p = re.compile(pattern)
            order_insert_dict = {'is_del':0, 'source':wherefrom} # 插入order表的一条记录字典
            lender_insert_dict = {'is_del':0} # 插入lender表中的一条记录字典
            try:
                if one_data[0]: # 订单编号 (必要唯一字段)
                    if Orders.select().where((Orders.disp == one_data[0]) & (Orders.is_del == 0)): #重复订单
                        exception_disp += ('重复订单: '+str(one_data[0])+' '+one_data[1]+'\n')
                        continue
                    order_insert_dict['disp'] = str(one_data[0])
                else:
                    exception_disp += ('订单号为空的订单: '+one_data[1]+'\n')
                    continue
                if one_data[8]: # 订单状态
                    if one_data[8] in statues_keys:
                        order_insert_dict['status'] = orderStatusKey[one_data[8]]
                    else:
                        pass
                        # exception_disp += ('订单状态格式错误 '+str(one_data[0])+' '+one_data[1]+' '+one_data[8]+'\n')
                        # continue
                if one_data[9]: # 账期
                    if one_data[9] in zhangaqi_keys:
                        order_insert_dict['account_day'] = str(one_data[9])
                    else:
                        pass
                        # exception_disp += ('账期格式错误 '+str(one_data[0])+' '+one_data[1]+' '+one_data[9]+'\n')
                        # continue
                if one_data[10]: # 产品名称
                    order_insert_dict['product'] = str(one_data[10])
                if one_data[11]: # 分期金额
                    order_insert_dict['amount'] = float(one_data[11])
                else:
                    pass
                    # exception_disp += ('分期金额为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    # continue
                if one_data[12]: # 首次还款日
                    if not p.match(one_data[12]):
                        pass
                        # exception_disp += ('首次还款日格式有误 '+str(one_data[0])+' '+one_data[1]+'\n')
                        # continue
                    else:
                        order_insert_dict['payment_day'] = one_data[12]
                else:
                    pass
                    # exception_disp += ('首次还款日为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    # continue
                if one_data[13]: # 月供
                    order_insert_dict['month_pay'] = float(one_data[13])
                else:
                    pass
                    # exception_disp += ('月供为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    # continue
                if one_data[14]: # 期数
                    order_insert_dict['periods'] = int(one_data[14])
                else:
                    # exception_disp += ('期数为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    # continue
                    pass
               
                if one_data[15] or int(one_data[15])==0: # 已付期数
                    order_insert_dict['paid_periods'] = int(one_data[15])
                else:
                    # exception_disp += ('已还分期数为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    # continue
                    pass
                if one_data[16]: # 订单日期
                    if not p.match(one_data[16]):
                        # exception_disp += ('订单日格式有误 '+str(one_data[0])+' '+one_data[1]+'\n')
                        # continue
                        pass
                    else:
                        order_insert_dict['order_date'] = one_data[16]
                if one_data[17]: # 接单日期
                    if not p.match(one_data[17]):
                        # exception_disp += ('接单日格式有误 '+str(one_data[0])+' '+one_data[1]+'\n')
                        # continue
                        pass
                    else:
                        order_insert_dict['takeorder_data'] = one_data[17]
                if one_data[18]: # 已还金额
                    order_insert_dict['received_amount'] = float(one_data[18])
                else:
                    pass
                    # exception_disp += ('已还金额为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    # continue
                    
                if one_data[19]: # 父母
                    order_insert_dict['parent'] = one_data[19]
                if one_data[20]: # 父母电话
                    order_insert_dict['parent_call'] = str(int(one_data[20]))
                if one_data[21]: # 同寝
                    order_insert_dict['roommate'] = one_data[21]
                if one_data[22]: # 同寝电话
                    order_insert_dict['roommate_call'] = str(int(one_data[22]))
                if one_data[23]: # 同学
                    order_insert_dict['classmate'] = str(one_data[23])
                if one_data[24]: # 同学电话
                    order_insert_dict['classmate_call'] = str(int(one_data[24]))
                
                order_insert_dict['create_time'] = datetime.datetime.now()
                order_insert_dict['modify_time'] = order_insert_dict['create_time']

                #################################################################
                logger.debug(one_data[1])
                if one_data[1]: # 姓名
                    lender_insert_dict['name'] = str(one_data[1])
                else:
                    exception_disp += ('姓名为空: '+str(one_data[0])+'\n')
                    continue
                if one_data[2]: # 电话
                    lender_insert_dict['tel'] = str(int(one_data[2]))
                else:
                    lender_insert_dict['tel'] = "0"
                if one_data[3]: # 身份证
                    # if Lender.select().where((Lender.idcard == one_data[3]) & (Lender.is_del == 0)): # 身份证重复
                    #     exception_disp += ('身份证重复: '+str(one_data[0])+' '+one_data[1]+'\n')
                    #     continue
                    lender_insert_dict['idcard'] = (str(one_data[3])).split('.')[0]
                else:
                    exception_disp += ('身份证为空的订单: '+str(one_data[0])+' '+one_data[1]+'\n')
                    continue
                    
                if one_data[4]: # 学院区域
                    lender_insert_dict['univers_area'] = one_data[4]
                else:
                    ender_insert_dict['univers_area'] = "NULL"
                if one_data[5]: # 学校
                    lender_insert_dict['university'] = one_data[5]
                else:
                    lender_insert_dict['university'] = "NULL"
                if one_data[6]: # 家庭区域
                    lender_insert_dict['family_area'] = one_data[6]
                else:
                    lender_insert_dict['family_area'] = "NULL"
                if one_data[7]: # 家庭住址
                    lender_insert_dict['family_addr'] = one_data[7]
                else:
                    lender_insert_dict['family_addr'] = "NULL"
            except BaseException,e:
                logger.error('解析失败订单: '+ str(one_data[0])+' '+one_data[1])
                logger.error(str(e))
                exception_disp += ('解析失败订单: '+ str(one_data[0])+' '+one_data[1]+'\n')
                continue

            # 插入数据库
            try:
                Lender.insert(lender_insert_dict).execute()
                order_insert_dict['lender'] = (Lender.select().where(Lender.idcard == lender_insert_dict['idcard']).get()).id
                Orders.insert(order_insert_dict).execute()
                success_insert_count += 1
            except BaseException,e:
                logger.error('插入数据库失败订单号: '+ str(one_data[0])+str(e))
                exception_disp += ('插入数据库失败订单号: '+ str(one_data[0])+'\n')

        if len(exception_disp)>0:
            exception_disp = '成功插入 {0}/{1} 条数据\n\n'.format(success_insert_count,nrows-1) + exception_disp
            return exception_disp
        else:
            return '成功插入 {0}/{1} 条数据'.format(success_insert_count,nrows-1)

        


    @staticmethod
    def save_orders_file():
        logger.debug('i am save_ordersource......')
        name = request.forms.name #订单来源名称
        file_md5 = request.forms.testmd5
        data = request.files.data
        ext  = data.filename.split('.')[-1] #上传文件后缀
        save_name = file_md5 + '.' + ext

        if resource.set_orders_path(name) :
            new_file=os.path.join(resource.get_orders_path,save_name)
            if not os.path.exists(new_file):
                data.filename=save_name
                data.save(resource.get_orders_path, overwrite=True)
                if resource.get_md5(new_file)==file_md5:
                    return OrderList.save_orders_to_database(new_file,name) # 解析表格
                else:
                    os.remove(new_file)
                    return '上传失败,请重新上传'
            else:
                return '文件已存在，请勿重复上传'
        else:
            return '创建路径失败'
