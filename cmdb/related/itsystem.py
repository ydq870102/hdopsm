#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
import base


class ItsystemRelated(base.BaseRelated):

    def __init__(self, sql_id=''):
        super(ItsystemRelated, self).__init__(ItSystem, sql_id)
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
            'itsystem_zone_list': base.get_related_foreignkey_count(ItSystem, 'related_zone_id_id', Zone),
            'itsystem_system_manager_list': base.get_related_column_count(ItSystem, 'system_manager'),
            'itsystem_system_admins_list': base. get_related_column_count(ItSystem, 'system_admin'),
        }

    def get_detail_related(self):
        return {
            'zone_label_list': base.get_related_attr(Zone, 'label_cn'),
            'itsystem_person_enum_list': base.get_related_column_enum('ItSystem', 'is_untrained_person_use'),
        }

    def get_related_related(self):
        self._set_sysdevice_instance()
        self._set_database_instance()
        self._set_process_instance()
        return {
            'sysdevice_list': self.sysdevice_instance, 'sysdevice_count': self.sysdevice_instance.count(),
            'process_list': self.process_instance, 'process_count': self.process_instance.count(),
            'database_list': self.database_instance, 'database_count': self.database_instance.count(),
        }

    def get_alarm_related(self):
        pass

    def get_record_related(self):
        pass
