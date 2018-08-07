#! /usr/bin/env python
#  encoding: utf-8

from cmdb.models import ItSystem, Zone
from utils.checkfun import *
import logging
import traceback
from utils.funnel import *

logger = logging.getLogger('django')
msg = []


def create(**kwargs):
    """
    @itsystem 创建方法
    :param kwargs:
    :return:
    """
    result = kwargs.get('result', {})
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(ItSystem, result, filter_data).funnel_create()
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
    itsystem 查询方法
    :param kwargs:
    :return:
    """
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(ItSystem, {}, filter_data).funnel_get()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        # filter_data['where']['is_delete'] = 0
        data = ItSystem.objects.filter(**filter_data['where']).values(*filter_data['output']).order_by(
            filter_data['order_by'])[0:filter_data['limit']]
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        return msg
    return data


def delete(**kwargs):
    where = kwargs.get("where", [])
    check_where_id(where)
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
    result = json.loads(kwargs.get("result", {}))
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(ItSystem, result, filter_data).funnel_update()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        ItSystem.objects.filter(**filter_data['where']).update(**result)
        return msg
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))
        return msg


def imp(**kwargs):
    result_list = kwargs.get('result', {})
    for result in result_list:
        covert_data = get_covert()
        filter_data = get_filter(eargs=covert_data)
        try:
            result = Funnel(ItSystem, result, filter_data).funnel_imp()
        except Exception, e:
            msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
            continue
        if ItSystem.objects.filter(itsystem_name=result['itsystem_name']).count() == 1:
            try:
                result['is_delete'] = 0
                ItSystem.objects.filter(itsystem_name=result['itsystem_name']).update(**result)
            except Exception, e:
                msg.append("sql 执行出错，错误原因: {}".format(e.message))
        else:
            try:
                ItSystem.objects.create(**result)
            except Exception, e:
                msg.append("sql 执行出错，错误原因: {}".format(e.message))
    return msg


def exp(**kwargs):
    """
    itsystem 导出方法
    :param kwargs:
    :return:
    """
    covert_data = get_covert()
    filter_data = get_filter(kwargs, covert_data)
    try:
        Funnel(ItSystem, {}, filter_data).funnel_exp()
    except Exception, e:
        msg.append("数据检查或者转换出错，错误原因为: {}".format(e.message))
        return msg
    try:
        # filter_data['where']['is_delete'] = 0
        data = ItSystem.objects.filter(**filter_data['where']).values(*filter_data['output']).order_by(
            filter_data['order_by'])[0:filter_data['limit']]
        return data
    except Exception, e:
        msg.append("sql 执行出错，错误原因: {}".format(e.message))


def get_covert():
    enum = ItSystem.get_enum_column()
    return {'enum': enum}
