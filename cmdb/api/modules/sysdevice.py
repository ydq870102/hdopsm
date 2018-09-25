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
    SysDevice 创建方法
    :param kwargs:
    :return: Message
    """
    try:
        result = FunnelIn(SysDevice, kwargs).funnel_create()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e))
        return msg
    try:
        SysDevice.objects.create(**result)
        msg.append('创建成功')
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e))


def get(**kwargs):
    """
    SysDevice 查询方法
    :param kwargs:
    :return: 查询集
    """
    try:
        where, output, order_by, limit = FunnelIn(SysDevice, kwargs).funnel_get()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e))
        return msg
    try:
        data = SysDevice.objects.filter(**where).values(*output).order_by(order_by)[0:limit]
        data = FunnelOut(SysDevice, data).convert()
    except Exception:
        msg.append("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        return msg
    return data


def search(**kwargs):
    """
    SysDevice 查询方法
    :param kwargs:
    :return: 查询集
    """

    try:
        where, output, order_by, limit = FunnelIn(SysDevice, kwargs).funnel_get()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e))
        return msg
    try:
        data = SysDevice.objects.filter(Q(**where)).values(*output).order_by(order_by)[0:limit]
        data = FunnelOut(SysDevice, data).convert()
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        return msg
    return data


def delete(**kwargs):
    """
    SysDevice 删除方法
    :param kwargs: 字典
    :return: Message
    """
    where = kwargs.get("where", [])
    if isinstance(where, dict):
        try:
            SysDevice.objects.filter(**where).update(is_delete=1)
        except Exception, e:
            msg.append("ID{}删除执行出错，错误原因: {}".format(where, e))
    if isinstance(where, list):
        for key in where:
            try:
                SysDevice.objects.filter(id=key).update(is_delete=1)
            except Exception, e:
                msg.append("ID{}删除执行出错，错误原因: {}".format(key, e))
    return msg


def update(**kwargs):
    """
    SysDevice
    :param kwargs:
    :return: Message
    """
    try:
        where, result = FunnelIn(SysDevice, kwargs).funnel_update()
    except Exception, e:
        logger.debug("数据检查或者转换出错，错误原因为: {}".format(traceback.format_exc()))
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e))
        return msg
    try:
        SysDevice.objects.filter(**where).update(**result)
        return msg
    except Exception, e:
        logger.debug("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        msg.append("sql 执行出错，错误原因: {}".format(e))
        return msg


def imp(**kwargs):
    """
    SysDevice 导入方法
    :param kwargs:
    :return: Message
    """
    result_dict ={}
    result_list = kwargs.get('result', {})
    for result in result_list:
        result_dict['result'] = result
        try:
            result = FunnelIn(SysDevice, result_dict).funnel_imp()
        except Exception, e:
            msg.append("数据检查或者转换出错，错误原因为: {}".format(e))
            continue
        if SysDevice.objects.filter(label_cn=result['label_cn']).count() == 1:
            try:
                result['is_delete'] = 0
                SysDevice.objects.filter(label_cn=result['label_cn']).update(**result)
            except Exception, e:
                logger.debug("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
                msg.append("sql 执行出错，错误原因: {}".format(e))
        else:
            try:
                SysDevice.objects.create(**result)
            except Exception, e:
                logger.debug("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
                msg.append("sql 执行出错，错误原因: {}".format(e))
    return msg


def exp(**kwargs):
    """
    SysDevice 导出方法
    :param kwargs:
    :return:
    """
    try:
        where, output, order_by, limit = FunnelIn(SysDevice, kwargs).funnel_exp()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e))
        return msg
    try:
        data = SysDevice.objects.filter(**where).values(*output).order_by(order_by)[0:limit]
        data = FunnelOut(SysDevice, data).convert()
        return data
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e))
