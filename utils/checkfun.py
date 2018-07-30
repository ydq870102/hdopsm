#! /usr/bin/env python
#  encoding: utf-8

from hdopsm.models import Enum
import logging
logger = logging.getLogger('django.request')


def check_exists_filed(model, kwargs):
    for filed in kwargs.keys():
        if not hasattr(model, filed):
            logger.error()
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
    for key in where:
        if not key.isdigit():
            raise Exception("执行条件ID必须为数字")


def check_column_enum(model, column, kwargs):
    enum_list = []
    enums = Enum.objects.filter(table_name=model, table_column=column).values('value_desc')
    for enum in enums:
        enum_list.append(enum['value_desc'])
    if kwargs[column] not in enum_list:
        raise Exception("{}字段{}的值必须为：{}".format(model, column, kwargs[column]))


def change_column_eum(model, column, kwargs):
    sql_filter = Enum.objects.filter(table_name=model, table_column=column, value_desc=kwargs[column])
    kwargs[column] =sql_filter[0].value
    return kwargs

