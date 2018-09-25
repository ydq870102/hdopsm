#! /usr/bin/env python
#  encoding: utf-8

from cmdb.models import *
import logging
import traceback
from cmdb.api.funnelin import *
from django.db.models import Q
from cmdb.api.funnelout import *

logger = logging.getLogger('django')
msg = []


def create(**kwargs):
    """
    ItSystem 创建方法
    :param kwargs:
    :return: Message
    """
    try:
        result = FunnelIn(ItSystem, kwargs).funnel_create()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        ItSystem.objects.create(**result)
        msg.append('创建成功')
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))


def get(**kwargs):
    """
    ItSystem 查询方法
    :param kwargs:
    :return: 查询集
    """
    try:
        where, output, order_by, limit = FunnelIn(ItSystem, kwargs).funnel_get()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        data = ItSystem.objects.filter(**where).values(*output).order_by(order_by)[0:limit]
        data = FunnelOut(ItSystem, data).convert()
    except Exception:
        msg.append("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        return msg
    return data


def search(**kwargs):
    """
    ItSystem 查询方法
    :param kwargs:
    :return: 查询集
    """

    try:
        where, output, order_by, limit = FunnelIn(ItSystem, kwargs).funnel_get()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        data = ItSystem.objects.filter(Q(**where)).values(*output).order_by(order_by)[0:limit]
        data = FunnelOut(ItSystem, data).convert()
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        return msg
    return data


def delete(**kwargs):
    """
    ItSystem 删除方法
    :param kwargs: 字典
    :return: Message
    """
    where = kwargs.get("where", [])
    if isinstance(where, dict):
        try:
            ItSystem.objects.filter(**where).update(is_delete=1)
        except Exception, e:
            msg.append("ID{}删除执行出错，错误原因: {}".format(where, e.message))
    if isinstance(where, list):
        for key in where:
            try:
                ItSystem.objects.filter(id=key).update(is_delete=1)
            except Exception, e:
                msg.append("ID{}删除执行出错，错误原因: {}".format(key, e.message))
    return msg


def update(**kwargs):
    """
    ItSystem 更新方法
    :param kwargs:
    :return: Message
    """
    try:
        where, result = FunnelIn(ItSystem, kwargs).funnel_update()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        ItSystem.objects.filter(**where).update(**result)
        return msg
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))
        return msg


def imp(**kwargs):
    """
    ItSystem 导入方法
    :param kwargs:
    :return: Message
    """
    result_dict ={}
    result_list = kwargs.get('result', {})
    for result in result_list:
        result_dict['result'] = result
        try:
            result = FunnelIn(ItSystem, result_dict).funnel_imp()
        except Exception, e:
            msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
            continue
        if ItSystem.objects.filter(label_cn=result['label_cn']).count() == 1:
            try:
                result['is_delete'] = 0
                ItSystem.objects.filter(label_cn=result['label_cn']).update(**result)
            except Exception, e:
                logger.debug("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
                msg.append("sql 执行出错，错误原因: {}".format(e.message))
        else:
            try:
                ItSystem.objects.create(**result)
            except Exception, e:
                logger.debug("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
                msg.append("sql 执行出错，错误原因: {}".format(e.message))
    return msg


def exp(**kwargs):
    """
    ItSystem 导出方法
    :param kwargs:
    :return:
    """
    try:
        where, output, order_by, limit = FunnelIn(ItSystem, kwargs).funnel_exp()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        data = ItSystem.objects.filter(**where).values(*output).order_by(order_by)[0:limit]
        data = FunnelOut(ItSystem, data).convert()
        return data
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))
