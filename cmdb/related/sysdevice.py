#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
import base


class SysdeviceRelated(base.BaseRelated):

    def __init__(self, sql_id=''):
        super(SysdeviceRelated, self).__init__(SysDevice, sql_id)
        self.get_instance()
        self.process_instance = []
        self.database_instance = []

    def _set_process_instance(self):
        try:
            self.process_instance = self.model_instance.process_set.all()
        except Exception:
            self.process_instance = []

    def _set_database_instance(self):
        try:
            self.database_instance = self.model_instance.database_set.all()
        except Exception:
            self.database_instance = []

    def get_list_related(self):
        return {
            'sysdevice_status_enum_list': base.get_related_column_enum('SysDevice', 'status'),
            'sysdevice_assets_type_enum_list': base.get_related_column_enum('SysDevice', 'assets_type'),
            'sysdevice_system_enum_list': base.get_related_column_enum('SysDevice', 'system'),
            'sysdevice_zone_list': base.get_related_foreignkey_count(SysDevice, 'related_zone_id_id', Zone),
            'sysdevice_itsystem_list': base.get_related_foreignkey_count(SysDevice, 'related_itsystem_id_id',
                                                                         ItSystem),
            'sysdevice_system_list': base.get_related_column_count(SysDevice, 'system'),
            'sysdevice_assets_type_list': base.get_related_column_count(SysDevice, 'assets_type')
        }

    def get_detail_related(self):
        return {'sysdevice_status_enum_list': base.get_related_column_enum('SysDevice', 'status'),
                'sysdevice_assets_type_enum_list': base.get_related_column_enum('SysDevice', 'assets_type'),
                'sysdevice_system_enum_list': base.get_related_column_enum('SysDevice', 'system'),
                'itsystem_label_list': base.get_related_attr(ItSystem, 'label_cn'),
                'zone_label_list': base.get_related_attr(Zone, 'label_cn'),
                'room_label_list': base.get_related_attr(Room, 'label_cn'),
                }

    def get_related_related(self):
        self._set_database_instance()
        self._set_process_instance()
        return {
            'process_list': self.process_instance, 'process_count': self.process_instance.count(),
            'database_list': self.database_instance, 'database_count': self.database_instance.count(),
        }

    def get_alarm_related(self):
        pass

    def get_record_related(self):
        pass
