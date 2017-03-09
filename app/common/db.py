#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from peewee import *
import ConfigParser
import os,sys

# 当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def read_conf(model):
    try:
        cf = ConfigParser.ConfigParser()
        if os.path.exists(os.path.join(get_path("",parent=True), "..", 'conf.ini')):
            cf.read(os.path.join(get_path("",parent=True), "..", 'conf.ini'))
            item = dict(cf.items(model))
            return dict(item)
        else:
            return {}
    except Exception as e:
        return {}

HOST='localhost'
PORT='3306'
USER='root'
PASSWD='123456'

dbconf = read_conf('db')
if dbconf:
    HOST=dbconf['host']
    PORT=dbconf['port']
    USER=dbconf['user']
    PASSWD=dbconf['password']

database = MySQLDatabase('dunning', **{'host': HOST, 'port': int(PORT), 'user': USER,'passwd':PASSWD})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Admin(BaseModel):
    enable = IntegerField(null=True)
    is_admin = IntegerField()
    name = CharField()
    passwd = CharField()
    user = CharField()

    class Meta:
        db_table = 'admin'

class Lender(BaseModel):
    family_addr = CharField(null=True)
    family_area = CharField(null=True)
    id = IntegerField(index=True)
    idcard = CharField(db_column='idcard_id')
    is_del = IntegerField()
    name = CharField()
    tel = CharField()
    univers_area = CharField(null=True)
    university = CharField(null=True)

    class Meta:
        db_table = 'lender'
        indexes = (
            (('id', 'idcard'), True),
        )
        primary_key = CompositeKey('id', 'idcard')

class Orders(BaseModel):
    account_day = CharField(null=True)
    amount = FloatField(null=True)
    call_details = CharField(null=True)
    classmate = CharField(null=True)
    classmate_call = CharField(null=True)
    contract = CharField(null=True)
    create_time = DateTimeField(null=True)
    disp = CharField(db_column='disp_id', null=True)
    is_del = IntegerField(null=True)
    lender = ForeignKeyField(db_column='lender_id', rel_model=Lender, to_field='id')
    lender_pic = CharField(null=True)
    modify_time = DateTimeField(null=True)
    month_pay = FloatField(null=True)
    order_date = DateField(null=True)
    paid_periods = IntegerField(null=True)
    parent = CharField(null=True)
    parent_call = CharField(null=True)
    payment_day = CharField(null=True)
    periods = IntegerField(null=True)
    product = CharField(null=True)
    received_amount = FloatField(null=True)
    roommate = CharField(null=True)
    roommate_call = CharField(null=True)
    source = CharField(null=True)
    status = IntegerField(null=True)
    takeorder_data = DateField(null=True)

    class Meta:
        db_table = 'orders'

class Files(BaseModel):
    order = ForeignKeyField(db_column='order_id', null=True, rel_model=Orders, to_field='id')
    path = CharField(null=True)
    time = DateTimeField(null=True)
    type = IntegerField(null=True)

    class Meta:
        db_table = 'files'

class Operation(BaseModel):
    admin = ForeignKeyField(db_column='admin_id', null=True, rel_model=Admin, to_field='id')
    after_status = IntegerField(null=True)
    before_status = IntegerField(null=True)
    files = CharField(null=True)
    is_change_status = IntegerField(null=True)
    is_upload = IntegerField(null=True)
    lender = ForeignKeyField(db_column='lender_id', null=True, rel_model=Lender, to_field='id')
    op_desc = CharField(null=True)
    time = DateTimeField(null=True)

    class Meta:
        db_table = 'operation'

class System(BaseModel):
    backuptime = TimeField(null=True)
    intval = IntegerField(null=True)
    passwd = CharField(null=True)
    username = CharField(null=True)

    class Meta:
        db_table = 'system'

