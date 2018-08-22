#! /usr/bin/env python
#  encoding: utf-8

from hdopsm.models import Enum
import json


class Funnel(object):

    def __init__(self, model=None, kwargs={}):
        self.model = model
        if isinstance(kwargs.get("result", {}),unicode):
            self.result = json.loads(kwargs.get("result", {}))
        else:
            self.result = kwargs.get("result", {})
        self.output = kwargs.get("output", [])
        self.limit = kwargs.get("limit", None)
        self.order_by = kwargs.get("order_by", "-id")
        self.where = kwargs.get("where", {})
        self.enum = []

    def is_exists_filed(self):
        for filed in self.result:
            if not hasattr(self.model, filed):
                raise CheckException("参数错误,{} 不在{}这张表里".format(self.model, filed))

    def is_exists_output_filed(self):
        if not isinstance(self.output, list):
            raise CheckException("参数错误,output{}必须为lIst".format(self.output))
        for field in self.output:
            if not hasattr(self.model, field):
                raise CheckException("{} 这个输出字段不存在".format(field))

    def check_order_by(self):
        if not hasattr(self.model, self.order_by.replace('-', '').lower()):
            raise CheckException("排序字段{}不在表{}中".format(self.order_by, self.model))

    def check_limit_type(self):
        if not str(self.limit).isdigit() and self.limit is not None:
            raise CheckException("limit 值必须为数字")

    def check_where_id(self):
        if isinstance(self.where, list):
            for key in self.where:
                if not key.isdigit():
                    raise Exception("where条件ID必须为数字")
        elif isinstance(self.where, dict):
            for key in self.where.values():
                if not key.isdigit:
                    raise CheckException("where条件ID必须为数字")

    def check_column_enum(self):

        for enum_dict in self.get_enum_column():
            for table_name, column in enum_dict.items():
                if not self.result.has_key(column):
                    continue
                enums = Enum.objects.filter(table_name=table_name, table_column=column).values('value_desc')
                enum_list = [enum['value_desc'] for enum in enums]
                if not isinstance(self.result, dict) or self.result[column] not in enum_list:
                    raise Exception("{}字段{}的枚举填写不正确，枚举类型为{}".format(self.model, column, enum_list))

    def change_date_filed(self):
        pass

    def get_enum_column(self):

        self.enum = Enum.objects.filter(table_name=self.model.__name__).values('table_name', 'table_column')
        return self.enum

    def funnel_get(self):
        self.is_exists_filed()
        self.is_exists_output_filed()
        self.check_limit_type()
        self.check_order_by()
        return self.where, self.output, self.order_by, self.limit

    def funnel_create(self):
        self.is_exists_filed()
        self.check_column_enum()
        return self.result

    def funnel_update(self):
        self.check_where_id()
        self.check_column_enum()
        return self.where, self.result

    def funnel_imp(self):
        self.is_exists_filed()
        self.check_column_enum()
        return self.result

    def funnel_exp(self):
        self.is_exists_filed()
        self.is_exists_output_filed()
        self.check_limit_type()
        self.check_order_by()
        return self.where, self.output, self.order_by, self.limit


class CheckException(Exception):

    def __init__(self, err='数据检查出错'):
        Exception.__init__(self, err)


class CovertException(Exception):

    def __init__(self, err='数据转换出错'):
        Exception.__init__(self, err)
