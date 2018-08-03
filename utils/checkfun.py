#! /usr/bin/env python
#  encoding: utf-8

from hdopsm.models import Enum
import logging
logger = logging.getLogger('django')


def check_exists_filed(model, kwargs):
    for filed in kwargs.keys():
        if not hasattr(model, filed):
            logger.error("参数错误,{} 不在{}这张表里".format(model, filed))
            raise Exception("参数错误,{} 不在{}这张表里".format(model, filed))


def check_output_filed(model, output):
    if not isinstance(output, list):
        logging.error("output 必须为list")
        raise Exception("output 必须为list")
    for field in output:
        if not hasattr(model, field):
            raise Exception("{} 这个输出字段不存在".format(field))
    else:
        return True


def check_order_by(model, order_by):
    if not hasattr(model, order_by.replace('-', '').lower()):
        raise Exception("排序字段不在表{}中".format(model))
    return True


def check_limit_type(limit):
    if str(limit).isdigit() or limit is None:
        return True
    else:
        raise Exception("limit 值必须为数字")


def check_where_id(where):
    if isinstance(where, list):
        for key in where:
            if not key.isdigit():
                raise Exception("执行条件ID必须为数字")
    elif isinstance(where, dict):
        for key in where.values():
            if not key.isdigit:
                raise Exception("执行条件ID必须为数字")


def check_column_enum(model, column, kwargs):
    enum_list = []
    enums = Enum.objects.filter(table_name=model, table_column=column).values('value_desc')
    for enum in enums:
        enum_list.append(enum['value_desc'])
    if isinstance(kwargs, list):
        for args in kwargs:
            if args[column] not in enum_list:
                    raise Exception("{}字段{}的枚举{}填写不正确".format(model, column, args[column]))
    elif isinstance(kwargs, dict):
        if kwargs[column] not in enum_list:
            raise Exception("{}字段{}的枚举填写不正确，枚举类型为{}".format(model, column, enum_list))
    else:
        raise Exception("更新数据{}类型{}不正确".format(kwargs, type(kwargs)))


def change_column_eum(model, column, kwargs):
    try:
        sql_filter = Enum.objects.filter(table_name=model, table_column=column, value_desc=kwargs[column])
        kwargs[column] =sql_filter[0].value
        return kwargs
    except Exception, e:
        raise Exception("字段{}枚举转换出错".format(column))

