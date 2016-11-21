from peewee import *

database = MySQLDatabase('dunning', **{'host': 'localhost', 'port': 3306, 'user': 'root', 'password':'123456'})

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
    classmate = CharField(null=True)
    classmate_call = CharField(null=True)
    family_addr = CharField(null=True)
    family_area = CharField(null=True)
    id = IntegerField()
    idcard = CharField(db_column='idcard_id')
    is_del = IntegerField()
    lender_pic = CharField(null=True)
    name = CharField()
    parent = CharField(null=True)
    parent_call = CharField(null=True)
    roommate = CharField(null=True)
    roommate_call = CharField(null=True)
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
    account_day = DateField(null=True)
    amount = IntegerField(null=True)
    call_details = CharField(null=True)
    contract = CharField(null=True)
    is_del = IntegerField(null=True)
    lender = ForeignKeyField(db_column='lender_id', rel_model=Lender, to_field='id')
    month_pay = CharField(null=True)
    order_date = DateField(null=True)
    paid_periods = IntegerField(null=True)
    periods = IntegerField(null=True)
    product = CharField(null=True)
    received_amount = CharField(null=True)
    source = CharField(null=True)
    status = IntegerField(null=True)
    takeorder_data = DateField(null=True)

    class Meta:
        db_table = 'orders'

class Operation(BaseModel):
    admin = ForeignKeyField(db_column='admin_id', null=True, rel_model=Admin, to_field='id')
    after_status = IntegerField(null=True)
    before_status = IntegerField(null=True)
    files = CharField(null=True)
    is_change_status = IntegerField(null=True)
    is_upload = IntegerField(null=True)
    order = ForeignKeyField(db_column='order_id', null=True, rel_model=Orders, to_field='id')
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

