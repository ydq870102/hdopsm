#! /usr/bin/env python
#  encoding: utf-8

from hdopsm.models import Enum
import json


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
        for enum_dict in self.filter['enum']:
            for table_name, column in enum_dict.items():
                enums = Enum.objects.filter(table_name=table_name, table_column=column).values('value_desc')
                enum_list = [enum['value_desc'] for enum in enums]
                if not isinstance(self.kwargs, dict) or self.kwargs[column] not in enum_list:
                    raise Exception("{}字段{}的枚举填写不正确，枚举类型为{}".format(self.model, column, enum_list))


    # def name_covert_foreigney(self):
    #
    #     for foreignkey_dict in self.filter['foreignkey']:
    #         for key, value in foreignkey_dict.items():
    #             try:
    #                 obj = _load_model_modules(key)
    #                 print value[1], self.kwargs[value[0]]
    #                 parms = {value[1]: self.kwargs[value[0]]}
    #                 self.kwargs[value[0]] = obj.objects.get(**parms)
    #             except Exception, e:
    #                 raise CovertException("关键对象{}外键{}不存在".format(key, self.kwargs[value[0]]))

    def funnel_get(self):
        self.is_exists_filed()
        self.is_exists_output_filed()
        self.check_limit_type()
        self.check_order_by()
        return self.kwargs,self.filter

    def funnel_create(self):
        self.is_exists_filed()
        self.check_column_enum()
        return self.kwargs, self.filter

    def funnel_delete(self):
        self.check_where_id()
        return self.kwargs, self.filter

    def funnel_update(self):
        self.check_where_id()
        self.check_column_enum()
        return self.kwargs, self.filter

    def funnel_imp(self):
        self.is_exists_filed()
        self.check_column_enum()
        return self.kwargs, self.filter

    def funnel_exp(self):
        self.is_exists_filed()
        self.is_exists_output_filed()
        self.check_limit_type()
        self.check_order_by()
        return self.kwargs, self.filter

class CheckException(Exception):

    def __init__(self, err='数据检查出错'):
        Exception.__init__(self, err)


class CovertException(Exception):

    def __init__(self, err='数据转换出错'):
        Exception.__init__(self, err)


def get_filter(kwargs={}, eargs={}):
    output = kwargs.get("output", [])
    limit = kwargs.get("limit", None)
    order_by = kwargs.get("order_by", "-id")
    where = kwargs.get("where", {})
    foreignkey = eargs.get('foreignkey', {})
    enum = eargs.get('enum')
    return {'output': output, "limit": limit, 'order_by': order_by, 'where': where,
            'foreignkey': foreignkey, 'enum': enum}


# def _load_model_modules(model):
#     modult_dirs = ['cmdb.models', 'hdopsm.models']
#     for model_dir in modult_dirs:
#         module = __import__(model_dir, globals(), locals(), [model], 0)
#         if hasattr(module, model):
#             return getattr(module, model)
#         else:
#             continue
