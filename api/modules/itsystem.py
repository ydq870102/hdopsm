#! /usr/bin/env python
#  encoding: utf-8

from cmdb.models import ItSystem
from api.modules.checkfun import *


def create(**kwargs):
    # 1 获取参数
    # 2 检查参数
    check_exists_filed(ItSystem, **kwargs)

    # 3传输数据库
    try:
        itsystem = ItSystem.objects.create(**kwargs)
    except Exception, e:
        print "commit error: {}".format(e.message)
        raise Exception("commit error: {}".format(e.message))
    return itsystem.itsystem_name


def get(**kwargs):
    # 整理条件
    output = kwargs.get("output", ())
    limit = kwargs.get("limit", None)
    order_by = kwargs.get("order_by", "-id")
    where = kwargs.get("where", {})
    # 验证output
    check_output_filed(ItSystem, output)
    # order
    check_order_by(ItSystem, order_by)

    # 验证limit
    check_limit_type(limit)
    data = ItSystem.objects.filter(**where).values(*output).order_by(order_by)[0:limit]

    return data


def delete(**kwargs):
    where = kwargs.get("where", {})



def update(**kwargs):

    pass