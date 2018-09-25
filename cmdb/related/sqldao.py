#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
from base import *



# itsystem查询下拉框变量获取入口
def get_itsystem_params_list():
    return {
        'itsystem_zone_list': get_object_column_foreignkey_count(ItSystem, 'related_zone_id_id', Zone),
        'itsystem_system_manager_list': get_object_column_count(ItSystem, 'system_manager'),
        'itsystem_system_admins_list': get_object_column_count(ItSystem, 'system_admin'),
    }


# itsystem编辑下拉框变量获取入口
def get_itsystem_params_detail():
    return {
        'zone_label_list': get_object_attr(Zone, 'label_cn'),
        'itsystem_person_enum_list': get_object_column_enum('ItSystem', 'is_untrained_person_use'),
    }


#itsystem关联变量获取入口
def get_itsystem_params_related():
    return {
        'zone_label_list': get_object_attr(Zone, 'label_cn'),
        'itsystem_person_enum_list': get_object_column_enum('ItSystem', 'is_untrained_person_use'),
    }





# host编辑下拉框变量获取入口
def get_sysdevice_params_detail():
    return {'sysdevice_status_enum_list': get_object_column_enum('SysDevice', 'status'),
            'sysdevice_assets_type_enum_list': get_object_column_enum('SysDevice', 'assets_type'),
            'sysdevice_system_enum_list': get_object_column_enum('SysDevice', 'system'),
            'itsystem_label_list': get_object_attr(ItSystem, 'label_cn'),
            'zone_label_list': get_object_attr(Zone, 'label_cn'),
            'room_label_list': get_object_attr(Room, 'label_cn'),
            }


# host查询下拉框变量获取入口
def get_sysdevice_params_list():
    return {
        'sysdevice_status_enum_list': get_object_column_enum('SysDevice', 'status'),
        'sysdevice_assets_type_enum_list': get_object_column_enum('SysDevice', 'assets_type'),
        'sysdevice_system_enum_list': get_object_column_enum('SysDevice', 'system'),
        'sysdevice_zone_list': get_object_column_foreignkey_count(SysDevice, 'related_zone_id_id', Zone),
        'sysdevice_itsystem_list': get_object_column_foreignkey_count(SysDevice, 'related_itsystem_id_id', ItSystem),
        'sysdevice_system_list': get_object_column_count(SysDevice, 'system'),
        'sysdevice_assets_type_list': get_object_column_count(SysDevice, 'assets_type')
    }


# process编辑下拉框变量获取入口
def get_process_params_detail():
    return {'itsystem_label_list': get_object_attr(ItSystem, 'label_cn'),
            'sysdevice_label_list': get_object_attr(SysDevice, 'label_cn'),
            'process_crole_enum_list': get_object_column_enum('Process', 'cluster_role'),
            }


# process查询下拉框变量获取入口
def get_process_params_list():
    return {
        'process_itsystem_list': get_object_column_foreignkey_count(Process, 'related_itsystem_id_id', ItSystem),
        'process_device_list': get_object_column_foreignkey_count(Process, 'related_device_id_id', SysDevice),
    }


# database编辑下拉框变量获取入口
def get_database_params_detail():
    return {'itsystem_label_list': get_object_attr(ItSystem, 'label_cn'),
            'sysdevice_label_list': get_object_attr(SysDevice, 'label_cn'),
            'database_crole_enum_list': get_object_column_enum('Database', 'cluster_role'),
            }


# database查询下拉框变量获取入口
def get_database_params_list():
    return {
        'database_itsystem_list': get_object_column_foreignkey_count(Database, 'related_itsystem_id_id', ItSystem),
        'database_device_list': get_object_column_foreignkey_count(Database, 'related_device_id_id', SysDevice),
    }
