#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : insert_test_data.py
# Author        : Ljz
# Created       : 18th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : insert test data
#*****************************************************************************

import os
import sys
import time


#当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    path='app'+os.sep+'common'
    return get_path(path)

execfile(common_path()+os.sep+'db.py')

def insert_user():
    sql_admin='insert Admin values (1,"admin","admin","123456",1,1);'
    sql_common='insert Admin values (2,"test","test","123456",0,1);'
    database.execute_sql(sql_admin)
    database.execute_sql(sql_common)

def insert_order():
    sql_list=[]
    for i in xrange(20):
        maccount_day = "M_"+str(i)
        mamount = 1000+i
        mcall_details = '/call/detail/path'
        mclassmate = '同学—'+str(i)
        mclassmate_call = '1350000'+str(i)
        mcontract = '/contract/file/path'
        mdisp = '123456'+str(i)
        mlender = i+1
        mlender_pic = '/lender/pictures/path'
        mmonth_pay = '66'+str(i)
        morder_date = '2016-12-'+str(i+1)
        mpaid_periods = i
        mparent = '父母—'+str(i)
        mparent_call = '15800000'+str(i)
        mperiods = 12
        mproduct = '产品名称—'+str(i)
        mreceived_amount = '110'
        mroommate = '同寝-'+str(i)
        mroommate_call = '13900000'+str(i)
        if i<10:
            msource = '淘宝'
        else:
            msource = '京东'
        if i<5:
            mstatus = 1
        if i <10:
            mstatus = 3
        if i <20:
            mstatus = 4
        mtakeorder_data = '2017-1-'+str(i+1)
        Orders.insert(
            account_day = maccount_day,
            amount = mamount,
            call_details = mcall_details,
            classmate = mclassmate,
            classmate_call = mclassmate_call,
            contract = mcontract,
            disp = mdisp,
            lender = mlender,
            lender_pic = mlender_pic,
            month_pay = mmonth_pay,
            order_date = morder_date,
            paid_periods = mpaid_periods,
            parent = mparent,
            parent_call = mparent_call,
            periods = mperiods,
            product = mproduct,
            received_amount = mreceived_amount,
            roommate = mroommate,
            roommate_call = mroommate_call,
            source = msource,
            status = mstatus,
            takeorder_data = mtakeorder_data
        ).execute()


def insert_lender():
    for i in xrange(20):
        testcard='32032119901111119'+str(i)
        testname="Test_"+str(i)
        test_tel='1377097664'+str(i)
        if i<10:
            testuniversity='中国传媒大学南广学院'
            testuniver_area='南京'
            testfamily_area='南京'
            testfamily_addr='江宁'
        else:
            testuniversity='徐州师范大学'
            testuniver_area='徐州'
            testfamily_area='徐州'
            testfamily_addr='云龙湖'
            
        Lender.insert(idcard=testcard,name=testname,tel=test_tel, university=testuniversity,
            univers_area=testuniver_area, family_addr=testfamily_addr,family_area=testfamily_area,is_del=0).execute()

def select_forgin_test():
    query = Lender.select().join(Orders).where(Orders.lender==1).get()
    print query.name

def do_insert(sql_cmd):
    time.sleep(0.1)
    database.execute_sql(sql_cmd)

def select_test():
    a=Admin.select().where(Admin.passwd=='123')
    print a[1].name

def test():
    d={'user':'qq','name':'haha','passwd':'123','is_admin':0,'enable':1}
    Admin.insert(d).execute()

select_forgin_test()

# insert_lender()
# insert_order()

