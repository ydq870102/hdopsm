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
    check_exists_filed(ItSystem, **result)
    try:
        itsystem = ItSystem.objects.create(**result)
    except Exception, e:
        logger.error("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
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
        logger.error("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        raise Exception("sql 执行出错，错误原因: {}".format(e.message))
    return data


def delete(**kwargs):
    where = kwargs.get("where", [])
    check_where_id(where)
    if isinstance(where, dict):
        try:
            ItSystem.objects.filter(**where).update(is_delete=1)
        except Exception, e:
            logger.error("ID{}删除执行出错，错误原因: {}".format(where, traceback.format_exc()))
            msg.append("ID{}删除执行出错，错误原因: {}".format(where, e.message))
    if isinstance(where, list):
        for key in where:
            try:
                ItSystem.objects.filter(id=key).update(is_delete=1)
            except Exception, e:
                logger.error("ID{}删除执行出错，错误原因: {}".format(key, traceback.format_exc()))
                msg.append("ID{}删除执行出错，错误原因: {}".format(key, e.message))
    return msg


def update(**kwargs):
    where = kwargs.get("where", {})
    result = kwargs.get("result", {})
    try:
        check_where_id(where)
        check_exists_filed(ItSystem, result)
        check_column_enum('ItSystem', 'is_untrained_person_use', result)
    except Exception, e:
        logger.error("检查导入值有误.错误为: {}".format(traceback.format_exc()))
        msg.append("检查导入值有误.错误为: {}".format(e.message))
        return msg
    try:
        ItSystem.objects.filter(**where).update(**result)
    except Exception, e:
        logger.error("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        msg.append("sql 执行出错，错误原因: {}".format(e.message))
    return msg


def imp(**kwargs):
    result_list = kwargs.get('result', {})
    for result in result_list:
        covert_data = get_covert()
        filter_data = get_filter({'result': result}, covert_data)

        try:
            Funnel(ItSystem, result, filter_data).funnel_imp()
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
        logger.error("sql 执行出错，错误原因: {}".format(traceback.format_exc()))
        raise Exception("sql 执行出错，错误原因: {}".format(e.message))
    return data


def get_covert():
    foreignkey = ItSystem.get_foreignkey_column()
    enum = ItSystem.get_enum_column()
    return {'foreignkey': foreignkey, 'enum': enum}
