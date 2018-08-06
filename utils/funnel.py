#! /usr/bin/env python
#  encoding: utf-8

from hdopsm.models import Enum


class Funnel(object):

    def __init__(self, model=None, kwargs={}, filter={}):
        self.model = model
        self.kwargs = kwargs
        self.filter = filter

    def is_exists_filed(self):
        for filed in self.kwargs.keys():
            if not hasattr(self.model, filed):
                raise CheckException("参数错误,{} 不在{}这张表里".format(self.model, filed))

    def is_exists_output_filed(self):
        if not isinstance(self.filter['output'], list):
            raise CheckException("参数错误,output{}必须为lIst".format(self.filter['output']))
        for field in self.filter['output']:
            if not hasattr(self.model, field):
                raise CheckException("{} 这个输出字段不存在".format(field))

    def check_order_by(self):
        if not hasattr(self.model, self.filter['order_by'].replace('-', '').lower()):
            raise CheckException("排序字段不在表{}中".format(self.model))

    def check_limit_type(self):
        if not str(self.filter['limit']).isdigit() and self.filter['limit'] is not None:
            raise CheckException("limit 值必须为数字")

    def check_where_id(self):
        if isinstance(self.filter['where'], list):
            for key in self.filter['where']:
                if not key.isdigit():
                    raise Exception("where条件ID必须为数字")
        elif isinstance(self.filter['where'], dict):
            for key in self.filter['where'].values():
                if not key.isdigit:
                    raise CheckException("where条件ID必须为数字")

    def check_column_enum(self):
        for column in self.filter['enum']:
            enums = Enum.objects.filter(table_name=self.model, table_column=column).values('value_desc')
            enum_list = [enum['value_desc'] for enum in enums]
            if isinstance(self.kwargs, list):
                for args in self.kwargs:
                    if args[column] not in enum_list:
                        raise Exception("{}字段{}的枚举{}填写不正确".format(self.model, column, args[column]))
            elif isinstance(self.kwargs, dict):
                if self.kwargs[column] not in enum_list:
                    raise Exception("{}字段{}的枚举填写不正确，枚举类型为{}".format(self.model, column, enum_list))

    def funnel_get(self):
        pass


class CheckException(Exception):

    def __init__(self, err='数据检查出错'):
        Exception.__init__(self, err)


class CovertException(Exception):

    def __init__(self, err='数据转换出错'):
        Exception.__init__(self, err)


def get_filter(output=[], limit=None, order_by="-id", where={}, foreignkey=[], enum=[]):
    return {'output': output, "limit": limit, 'order_by': order_by, 'where': where, 'foreignkey': foreignkey,
            'enum': enum}
