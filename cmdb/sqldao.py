#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
from hdopsm.models import *
from django.db.models import Count


# itsystem下拉框变量获取入口
def get_itsystem_params_list():
    zones = get_itsystem_zone()
    system_managers = get_itsystem_system_manager()
    system_admins = get_itsystem_system_admin()
    return {'zones': zones, 'system_managers': system_managers, 'system_admins': system_admins}


def get_itsystem_zone():
    """
    信息系统界面所属区域项
    :return:
    """
    zone_list = ItSystem.objects.all().filter(is_delete=0).values('zone').order_by('zone').annotate(
        zone_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['zone'] = item['zone']
        temp['zone_count'] = item['zone_count']
        data.append(temp)
    return data


def get_itsystem_system_manager():
    """
    信息系统界面系统管理员
    :return:
    """
    zone_list = ItSystem.objects.all().filter(is_delete=0).values('system_manager').order_by('system_manager').annotate(
        system_manager_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['system_manager'] = item['system_manager']
        temp['system_manager_count'] = item['system_manager_count']
        data.append(temp)
    return data


def get_itsystem_system_admin():
    """
    信息系统界面系统负责人
    :return:
    """
    zone_list = ItSystem.objects.all().filter(is_delete=0).values('system_admin').order_by('system_admin').annotate(
        system_admin_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['system_admin'] = item['system_admin']
        temp['system_admin_count'] = item['system_admin_count']
        data.append(temp)
    return data


# host编辑下拉框变量获取入口
def get_host_params_detail():
    host_status_enum_list = get_host_status_enum()
    host_type_enum_list = get_host_type_enum()
    host_system_enum_list = get_host_system_enum()
    itsystem_name = get_itsystem_name()

    return {'host_status_enum_list': host_status_enum_list, 'host_type_enum_list': host_type_enum_list,
            'host_system_enum_list': host_system_enum_list, 'itsystem_name': itsystem_name}


# host查询下拉框变量获取入口
def get_host_params_list():
    host_status_enum_list = get_host_status_enum()
    host_type_enum_list = get_host_type_enum()
    host_system_enum_list = get_host_system_enum()
    host_zone_list = get_host_zone()
    host_itsystem_list = get_host_itsystem()
    print host_zone_list
    return {'host_status_enum_list': host_status_enum_list, 'host_type_enum_list': host_type_enum_list,
            'host_system_enum_list': host_system_enum_list, 'host_zone_list': host_zone_list,
            'host_itsystem_list': host_itsystem_list}


def get_host_status_enum():
    """
    下拉框主机状态枚举
    :return:
    """
    host_status_list = Enum.objects.filter(table_name='Host', table_column='status').values('value_desc')
    data = []
    for item in host_status_list:
        data.append(item['value_desc'])
    return data


def get_host_type_enum():
    """
    下拉框主机类型枚举
    :return:
    """
    host_type_list = Enum.objects.filter(table_name='Host', table_column='assets_type').values('value_desc')
    data = []
    for item in host_type_list:
        data.append(item['value_desc'])
    return data


def get_host_system_enum():
    """
    下拉框主机系统类型枚举
    :return:
    """
    host_type_list = Enum.objects.filter(table_name='Host', table_column='system').values('value_desc')
    data = []
    for item in host_type_list:
        data.append(item['value_desc'])
    return data


def get_itsystem_name():
    """
    下拉框主机信息系统类型
    :return:
    """
    itsystem_name_list = ItSystem.objects.all().values('label_cn')
    data = []
    for item in itsystem_name_list:
        data.append(item['label_cn'])
    return data


def get_host_zone():
    """
    信息系统界面所属区域项
    :return:
    """
    zone_list = Host.objects.all().filter(is_delete=0).values('zone').order_by('zone').annotate(
        zone_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['zone'] = item['zone']
        temp['zone_count'] = item['zone_count']
        data.append(temp)
    return data


def get_host_itsystem():
    """
    信息系统界面所属区域项
    :return:
    """
    zone_list = Host.objects.all().filter(is_delete=0).values('itsystem').order_by('itsystem').annotate(
        itsystem_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['itsystem'] = item['itsystem']
        temp['itsystem_count'] = item['itsystem_count']
        data.append(temp)
    return data
