#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
from hdopsm.models import *
from django.db.models import Count


def get_object_column_count(model, column):
    """
    @ 对象字段统计
    :param model:
    :param column:
    :return:
    """
    if hasattr(model, column):
        column_list = model.objects.all().filter(is_delete=0).values(column).order_by(column).annotate(
            column_count=Count('id'))
        data = []
        for item in column_list:
            temp = {}
            temp['column'] = item[column]
            temp['column_count'] = item['column_count']
            data.append(temp)
        return data


def get_object_column_enum(model, column):
    """
    @ 对象字段枚举
    :return:
    """
    if hasattr(model, column):
        column_list = Enum.objects.filter(table_name=model, table_column=column).values('value_desc')
        data = []
        for item in column_list:
            data.append(item['value_desc'])
        return data


def get_object_attr(model, column):
    """
    下拉框主机信息系统类型
    :return:
    """
    if hasattr(model, column):
        data_list = model.objects.all().values(column)
        data = []
        for item in data_list:
            data.append(item[column])
        return data


# itsystem下拉框变量获取入口
def get_itsystem_params_list():
    return {
        'host_zone_list': get_object_column_count(ItSystem, 'zone'),
        'host_system_manager_list': get_object_column_count(ItSystem, 'system_manager'),
        'host_system_admins_list': get_object_column_count(ItSystem, 'system_admin')
    }


# host编辑下拉框变量获取入口
def get_sysdevice_params_detail():
    return {'sysdevice_status_enum_list': get_object_column_enum(SysDevice, 'status'),
            'sysdevice_assets_type_enum_list': get_object_column_enum(SysDevice, 'assets_type'),
            'sysdevice_system_enum_list': get_object_column_enum(SysDevice, 'system'),
            'itsystem_label_list': get_object_attr(ItSystem, 'label_cn')
            }


# host查询下拉框变量获取入口
def get_sysdevice_params_list():
    return {
        'sysdevice_status_enum_list': get_object_column_enum(SysDevice, 'status'),
        'sysdevice_assets_type_enum_list': get_object_column_enum(SysDevice, 'assets_type'),
        'sysdevice_system_enum_list': get_object_column_enum(SysDevice, 'system'),
        'sysdevice_zone_list': get_object_column_count(SysDevice, 'zone'),
        'sysdevice_itsystem_list': get_object_column_count(SysDevice, 'related_itsystem_id'),
        'sysdevice_system_list': get_object_column_count(SysDevice, 'system'),
        'sysdevice_assets_type_list': get_object_column_count(SysDevice, 'assets_type')
    }
