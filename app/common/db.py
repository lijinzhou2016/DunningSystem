#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

from peewee import *
import os
import yaml
import json


path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config_file = os.path.join(path, "config", "conf.yml")
db_conf = yaml.load(file(config_file))

HOST = db_conf.get("db_host")
PORT = db_conf.get("db_port")
USER = db_conf.get("db_user")
PASSWD = db_conf.get("db_password")
DB_NAME = db_conf.get("db_name")


database = MySQLDatabase(DB_NAME, **{'host': HOST, 'port': int(PORT), 'user': USER, 'passwd': str(PASSWD)})


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class Admin(BaseModel):
    enable = IntegerField(null=True)
    is_admin = IntegerField(default=0)
    name = CharField(max_length=20)
    passwd = CharField(max_length=20)
    user = CharField(max_length=20)

    class Meta:
        db_table = 'admin'


class Lender(BaseModel):
    family_addr = CharField(null=True, max_length=200)
    family_area = CharField(null=True, max_length=100)
    idcard = CharField(db_column='idcard_id')
    is_del = IntegerField(default=0)
    name = CharField(max_length=20)
    tel = CharField(max_length=11)
    univers_area = CharField(null=True, max_length=100)
    university = CharField(null=True, max_length=100)

    class Meta:
        db_table = 'lender'


class Orders(BaseModel):
    account_day = CharField(null=True, max_length=50)
    amount = FloatField(null=True)
    call_details = CharField(null=True, max_length=100)
    classmate = CharField(null=True, max_length=20)
    classmate_call = CharField(null=True, max_length=20)
    contract = CharField(null=True, max_length=100)
    create_time = DateTimeField(null=True)
    disp = CharField(db_column='disp_id', null=True, max_length=100)
    is_del = IntegerField(null=True)
    lender = ForeignKeyField(Lender, db_column='lender_id', null=True, on_delete='CASCADE', to_field="id")
    lender_pic = CharField(null=True, max_length=100)
    modify_time = DateTimeField(null=True)
    month_pay = FloatField(null=True)
    order_date = DateField(null=True)
    paid_periods = IntegerField(null=True)
    parent = CharField(null=True, max_length=100)
    parent_call = CharField(null=True, max_length=100)
    payment_day = CharField(null=True, max_length=100)
    periods = IntegerField(null=True)
    product = CharField(null=True, max_length=100)
    received_amount = FloatField(null=True)
    roommate = CharField(null=True, max_length=100)
    roommate_call = CharField(null=True, max_length=100)
    source = CharField(null=True, max_length=100)
    status = IntegerField(null=True)
    takeorder_data = DateField(null=True)

    class Meta:
        db_table = 'orders'


class Files(BaseModel):
    order = ForeignKeyField(Orders, db_column='order_id', null=True, to_field="id")
    path = CharField(null=True, max_length=200)
    time = DateTimeField(null=True)
    type = IntegerField(null=True)

    class Meta:
        db_table = 'files'

    def __unicode__(self):
        return self.order


class Operation(BaseModel):
    admin = ForeignKeyField(Admin, db_column='admin_id', null=True, on_delete='CASCADE', to_field="id")
    after_status = IntegerField(null=True)
    before_status = IntegerField(null=True)
    files = CharField(null=True, max_length=200)
    is_change_status = IntegerField(null=True)
    is_upload = IntegerField(null=True)
    lender = ForeignKeyField(Lender, db_column='lender_id', null=True, on_delete='CASCADE', to_field="id")
    op_desc = CharField(null=True, max_length=300)
    time = DateTimeField(null=True)

    class Meta:
        db_table = 'operation'

    def __unicode__(self):
        return self.admin


class System(BaseModel):
    backuptime = TimeField(null=True)
    intval = IntegerField(null=True)
    passwd = CharField(null=True, max_length=20)
    username = CharField(null=True, max_length=20)

    class Meta:
        db_table = 'system'

    def __unicode__(self):
        return self.intval


if __name__ == "__main__":
    database.create_tables([Admin, Lender, Orders, Orders, Files, Operation, System])

