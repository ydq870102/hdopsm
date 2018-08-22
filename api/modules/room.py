#! /usr/bin/env python
#  encoding: utf-8

from cmdb.models import *
from utils.checkfun import *
import logging
import traceback
from api.funnel import *
from django.db.models import Q

logger = logging.getLogger('django')
msg = []


def create(**kwargs):
    """
    Room 创建方法
    :param kwargs:
    :return: Message
    """
    result = kwargs.get('result', {})
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(Room, result, filter_data).funnel_create()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        Room.objects.create(**result)
        msg.append('创建成功')
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))


def get(**kwargs):
    """
    Room 查询方法
    :param kwargs:
    :return: 查询集
    """
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(Room, {}, filter_data).funnel_get()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        # filter_data['where']['is_delete'] = 0
        data = Room.objects.filter(**filter_data['where']).values(*filter_data['output']).order_by(
            filter_data['order_by'])[0:filter_data['limit']]
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        return msg
    return data


def search(**kwargs):
    """
    Room 查询方法
    :param kwargs:
    :return: 查询集
    """
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(Room, {}, filter_data).funnel_get()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        data = Room.objects.filter(Q(**filter_data['where'])).values(*filter_data['output']).order_by(
            filter_data['order_by'])[0:filter_data['limit']]
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        return msg
    return data


def delete(**kwargs):
    """
    Room 删除方法
    :param kwargs: 字典
    :return: Message
    """
    where = kwargs.get("where", [])
    check_where_id(where)
    if isinstance(where, dict):
        try:
            Room.objects.filter(**where).update(is_delete=1)
        except Exception, e:
            msg.append("ID{}删除执行出错，错误原因: {}".format(where, e.message))
    if isinstance(where, list):
        for key in where:
            try:
                Room.objects.filter(id=key).update(is_delete=1)
            except Exception, e:
                msg.append("ID{}删除执行出错，错误原因: {}".format(key, e.message))
    return msg


def update(**kwargs):
    """
    Room 更新方法
    :param kwargs:
    :return: Message
    """
    result = json.loads(kwargs.get("result", {}))
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(Room, result, filter_data).funnel_update()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        Room.objects.filter(**filter_data['where']).update(**result)
        return msg
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))
        return msg


def imp(**kwargs):
    """
    Room 导入方法
    :param kwargs:
    :return: Message
    """
    result_list = kwargs.get('result', {})
    for result in result_list:
        covert_data = get_covert()
        filter_data = get_filter(eargs=covert_data)
        try:
            result, filter_data = Funnel(Room, result, filter_data).funnel_imp()
        except Exception, e:
            msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
            continue
        if Room.objects.filter(label_cn=result['label_cn']).count() == 1:
            try:
                result['is_delete'] = 0
                Room.objects.filter(label_cn=result['label_cn']).update(**result)
            except Exception, e:
                logger.debug("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
                msg.append("sql 执行出错，错误原因: {}".format(e.message))
        else:
            try:
                print result
                Room.objects.create(**result)
            except Exception, e:
                logger.debug("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
                msg.append("sql 执行出错，错误原因: {}".format(e.message))
    return msg


def exp(**kwargs):
    """
    Room 导出方法
    :param kwargs:
    :return:
    """
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(Room, {}, filter_data).funnel_exp()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        data = Room.objects.filter(**filter_data['where']).values(*filter_data['output']).order_by(
            filter_data['order_by'])[0:filter_data['limit']]
        return data
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))
