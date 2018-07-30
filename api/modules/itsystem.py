#! /usr/bin/env python
#  encoding: utf-8

from cmdb.models import ItSystem
from utils.checkfun import *
import logging

logger = logging.getLogger('django.request')


def create(**kwargs):
    """
    @itsystem 创建方法
    :param kwargs:
    :return:
    """
    result = kwargs.get('result', {})
    check_exists_filed(ItSystem, **result)
    try:
        itsystem = ItSystem.objects.create(**result)
    except Exception, e:
        logger.error("sql 执行出错，错误原因: {}".format(e.message))
        raise Exception("sql 执行出错，错误原因: {}".format(e.message))
    return itsystem.id


def get(**kwargs):
    """
    itsystem 查询方法
    :param kwargs:
    :return:
    """
    output = kwargs.get("output", ())
    limit = kwargs.get("limit", None)
    order_by = kwargs.get("order_by", "-id")
    where = kwargs.get("where", {})
    check_output_filed(ItSystem, output)
    check_order_by(ItSystem, order_by)
    check_limit_type(limit)
    try:
        data = ItSystem.objects.filter(**where).values(*output).order_by(order_by)[0:limit]
    except Exception, e:
        logger.error("sql 执行出错，错误原因: {}".format(e.message))
        raise Exception("sql 执行出错，错误原因: {}".format(e.message))
    return data


def delete(**kwargs):
    where = kwargs.get("where", [])
    check_where_id(where)
    msg = []
    if isinstance(where, dict):
        try:
            obj = ItSystem.objects.filter(where).update(is_delete=1)
        except Exception, e:
            logger.error("ID{}删除执行出错，错误原因: {}".format(obj.id, e.message))
            msg.append("ID{}删除执行出错，错误原因: {}".format(obj.id, e.message))
    if isinstance(where, list):
        for key in where:
            try:
                ItSystem.objects.filter(id=key).update(is_delete=1)
            except Exception, e:
                logger.error("ID{}删除执行出错，错误原因: {}".format(key, e.message))
                msg.append("ID{}删除执行出错，错误原因: {}".format(key, e.message))
    return msg


def update(**kwargs):
    where = kwargs.get("where", {})
    result = kwargs.get("result", {})
    check_where_id(where)
    check_exists_filed(ItSystem, **result)
    try:
        obj = ItSystem.objects.filter(where).update(**result)
    except Exception, e:
        logger.error("sql 执行出错，错误原因: {}".format(e.message))
        raise Exception("sql 执行出错，错误原因: {}".format(e.message))
    return obj.id


def imp(**kwargs):
    data_list = kwargs.get("result", [])
    msg = []
    for data in data_list:
        try:
            check_exists_filed(ItSystem, data)
            check_column_enum('ItSystem', 'is_untrained_person_use', data)
            data = change_column_eum('ItSystem', 'is_untrained_person_use', data)
        except Exception,e:
            logger.error("检查导入值有误.错误为: {}".format(e.message))
            msg.append("检查导入值有误.错误为: {}".format(e.message))
        if ItSystem.objects.filter(itsystem_name=data['itsystem_name']).count() == 1:
            try:
                data['is_delete'] = 0
                ItSystem.objects.filter(itsystem_name=data['itsystem_name']).update(**data)
            except Exception, e:
                print e.message
                logger.error("sql 执行出错，错误原因: {}".format(e.reason))
                msg.append("sql 执行出错，错误原因: {}".format(e.reason))
        else:
            try:
                ItSystem.objects.create(**data)
            except Exception, e:
                logger.error("sql 执行出错，错误原因: {}".format(e.message))
                msg.append("sql 执行出错，错误原因: {}".format(e.message))
    return msg
