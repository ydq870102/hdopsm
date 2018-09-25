#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
import base


class DatabaseRelated(base.BaseRelated):

    def __init__(self, sql_id=''):
        super(DatabaseRelated, self).__init__(Database, sql_id)
        self.get_instance()
        self.sysdevice_instance = []
        self.process_instance = []
        self.database_instance = []

    def _set_sysdevice_instance(self):
        try:
            self.sysdevice_instance = self.model_instance.sysdevice_set.all()
        except Exception:
            self.sysdevice_instance = []

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
            'database_itsystem_list': base.get_related_foreignkey_count(Database, 'related_itsystem_id_id', ItSystem),
            'database_device_list': base.get_related_foreignkey_count(Database, 'related_device_id_id', SysDevice),
        }

    def get_detail_related(self):
        return {'itsystem_label_list': base.get_related_attr(ItSystem, 'label_cn'),
                'sysdevice_label_list': base.get_related_attr(SysDevice, 'label_cn'),
                'database_crole_enum_list': base.get_related_column_enum('Database', 'cluster_role'),
                }

    def get_related_related(self):
        return {}

    def get_alarm_related(self):
        pass

    def get_record_related(self):
        pass
