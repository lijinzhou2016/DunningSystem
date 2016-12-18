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
        'order_shxx': ''
    }

class OrderList:
    def __init__(self, pageindex, userinfo, condition):
        self.pageindex = pageindex
        self.condition = int(condition)
        self.userinfo = userinfo    # 用户信息
        self.orders_return_info = {'userinfo':{},'fenyeinfo':{}, 'orders_list':[], 'condition':{}}   # 返回字典
        self.orders_one_info={'name':'','detailurl':'','ordernumber':'','phone':'','qiankuan':'','orderdata':'','acquiringdata':'','school':'','state':''}
        self.orders_return_info['userinfo']=self.userinfo
        if self.condition == 0:
            self.orders_count = Orders.select().count()   # 订单总条数
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
        else:
            self.orders_count = 0
            self.total_pages = 0
            self.orders_list_info =[]
    
    def set_orders_data(self):
        if self.condition == 1:
            self.condition_data()
        else:
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
            'order_shxx': bottle.request.query.order_shxx
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
        if len(condition_item['order_jtzz'] + condition_item['order_username'] + condition_item['order_school'] + condition_item['order_jtqy'])>0:
            logger.debug('select lender ... ')
            lender_query = Lender.select().where(   
                Lender.name.contains(condition_item['order_username']),
                Lender.university.contains(condition_item['order_school']),
                Lender.family_addr.contains(condition_item['order_jtzz']),
                Lender.family_area.contains(condition_item['order_jtqy'])
            )

            # 按条件查询到的数据，取出id添加到lender_id
            if len(lender_query)>=1:  
                for lender in lender_query:
                    lender_id.append(lender.id)
            else: 
                lender_flag = 1 # 表示按照搜索条件没有查询到数据

        if condition_item['order_zhangqi']: # 账期
            account_day_query = Orders.select().where(Orders.account_day == condition_item['order_zhangqi']).order_by(-Orders.create_time, -Orders.modify_time)
            temp_query.append(account_day_query) 
        if condition_item['order_shxx']: # 接单日期
            logger.debug('查询接单日期字段：'+condition_item['order_shxx'])
            takeorder_data_query = Orders.select().where(Orders.takeorder_data == condition_item['order_shxx']).order_by(-Orders.create_time, -Orders.modify_time)
            logger.debug(len(takeorder_data_query))
            temp_query.append(takeorder_data_query)
        if condition_item['order_ddzt']: # 订单状态
            status_query = Orders.select().where(Orders.status == orderStatusKey[condition_item['order_ddzt']]).order_by(-Orders.create_time, -Orders.modify_time)
            temp_query.append(status_query)
        if condition_item['order_jdrq']: # 订单日期
            order_date_query = Orders.select().where(Orders.order_date == condition_item['order_jdrq']).order_by(-Orders.create_time, -Orders.modify_time)
            temp_query.append(order_date_query)
        
        logger.debug(len(temp_query))
        if len(temp_query)>0: # 在orders表中查询到数据
            # 取交集
            orders_query = list(set(temp_query[0]).intersection(*temp_query[1:]))
            if len(orders_query)==0: # 若无交集，说明搜索条件有冲突，无数据
                orders_flag = 1

        
        if lender_flag == 1 or orders_flag == 1: # 说明查询条件有冲突，没有查到数据
            self.orders_return_info['orders_list'].append(self.orders_one_info)

        elif len(orders_query)>0 and len(lender_id)>0: # 两个表均有查到数据
            for id_tmp in lender_id: # 依次取出lender表中搜索到的记录id
                for query_tmp in orders_query: # 取出orders表中搜索到的记录
                    if query_tmp.lender_id == id_tmp: # 若id相等，则保存
                        self.orders_list_info.append(query_tmp) # 搜索的最终数据 ！！！

        elif len(orders_query)>0: # orders 表中查到数据
            self.orders_list_info = orders_query # 搜索的最终数据 ！！！

        else: # lender表中查到数据
            self.orders_list_info = Orders.select().where(Orders.lender_id << lender_id).order_by(-Orders.create_time, -Orders.modify_time) # 搜索的最终数据 ！！！
        
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
            
            # 计算总欠款
            def total_debt():
                month_pay = float(order_info_tmp.month_pay) # 月供
                periods = int(order_info_tmp.periods) # 期数
                paid_periods = int(order_info_tmp.paid_periods) # 已还期数
                amount = float(order_info_tmp.amount) # 分期金额
                payment_day = order_info_tmp.payment_day # 首次还款日

                payment_day_list = payment_day.split('-') # 格式如： ['2016', '12', '10']
                if int(payment_day_list[1]) + int(paid_periods) > 12:
                    payment_day_list[0] = str(int(payment_day_list[0])+1)
                    payment_day_list[1] = str(int(payment_day_list[1])+int(paid_periods)-12)
                else:
                    payment_day_list[1] = str(int(payment_day_list[1])+int(paid_periods))

                # 计算逾期天数的起始日期：
                laste_day = datetime.date(int(payment_day_list[0]),int(payment_day_list[1]),int(payment_day_list[2]))
                # 当前日期
                today = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

                over_day = (today - laste_day).days #逾期天数

                # 计算滞纳金
                if over_day > 0:
                    if over_day >90:
                        late_fee = (month_pay*0.26/30.0)*90+(month_pay*0.50/30.0)*(over_day-90)
                    else:
                        late_fee = (month_pay*0.26/30.0)*over_day
                else:
                    late_fee = 0.0

                # 总欠款
                debt = month_pay*(periods - paid_periods)+late_fee
                return round(debt, 2) #保留两位小数

            self.orders_return_info['orders_list'].append({
                'name' : lender_query.name,
                'detailurl' : r'/orderdetail/'+ str(order_info_tmp.id) + r'?session=' + self.userinfo['session'],
                'ordernumber' : order_info_tmp.disp,
                'phone' : lender_query.tel,
                'qiankuan' : total_debt(), # 需要计算
                'orderdata' : order_info_tmp.order_date,
                'acquiringdata' : order_info_tmp.takeorder_data,
                'school' : lender_query.university,
                'state' : orderStatus[order_info_tmp.status]
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
        if not title == order_file_title:
            os.remove(filepath)
            return '文件模版错误，请核对后重新上传'

        for one_data in total_datas:
            
            try:
                if one_data[0]: # 订单编号 (必要唯一字段)
                    if Orders.select().where(Orders.disp == one_data[0]): #重复订单
                        exception_disp += ('重复订单: '+str(one_data[0])+' '+one_data[1]+'\n')
                        continue
                    order_insert_dict['disp'] = str(one_data[0])
                else:
                    exception_disp += ('订单号为空的订单: '+one_data[1]+'\n')
                    continue
                if one_data[8]: # 订单状态
                    order_insert_dict['status'] = orderStatusKey[one_data[8]]
                if one_data[9]: # 账期
                    order_insert_dict['account_day'] = str(one_data[9])
                if one_data[10]: # 产品名称
                    order_insert_dict['product'] = one_data[10]
                if one_data[11]: # 分期金额
                    order_insert_dict['amount'] = int(one_data[11])
                else:
                    exception_disp += ('分期金额为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    continue
                if one_data[12]: # 首次还款日
                    order_insert_dict['payment_day'] = one_data[12]
                else:
                    exception_disp += ('首次还款日为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    continue
                if one_data[13]: # 月供
                    order_insert_dict['month_pay'] = str(one_data[13])
                else:
                    exception_disp += ('月供为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    continue
                if one_data[14]: # 期数
                    order_insert_dict['periods'] = int(one_data[14])
                else:
                    exception_disp += ('期数为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    continue
                if one_data[15]: # 已付期数
                    order_insert_dict['paid_periods'] = int(one_data[15])
                else:
                    exception_disp += ('已还分期金额为空： '+str(one_data[0])+' '+one_data[1]+'\n')
                    continue
                if one_data[16]: # 订单日期
                    order_insert_dict['order_date'] = one_data[16]
                if one_data[17]: # 接单日期
                    order_insert_dict['takeorder_data'] = one_data[17]
                if one_data[18]: # 已还金额
                    order_insert_dict['received_amount'] = int(one_data[18])
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

                if one_data[1]: # 姓名
                    lender_insert_dict['name'] = one_data[1]
                if one_data[2]: # 电话
                    lender_insert_dict['tel'] = str(int(one_data[2]))
                if one_data[3]: # 身份证
                    lender_insert_dict['idcard'] = (str(one_data[3])).split('.')[0]
                if one_data[4]: # 学院区域
                    lender_insert_dict['univers_area'] = one_data[4]
                if one_data[5]: # 学校
                    lender_insert_dict['university'] = one_data[5]
                if one_data[6]: # 家庭区域
                    lender_insert_dict['family_area'] = one_data[6]
                if one_data[7]: # 家庭住址
                    lender_insert_dict['family_addr'] = one_data[7]
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
            exception_disp += '成功插入 {0}/{1} 条数据'.format(success_insert_count,nrows)
            return exception_disp
        else:
            return '成功插入 {0}/{1} 条数据'.format(success_insert_count,nrows)

        


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
