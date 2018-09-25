#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
import base


class ZoneRelated(base.BaseRelated):

    def __init__(self, sql_id=''):
        super(ZoneRelated, self).__init__(Zone, sql_id)
        self.get_instance()
        self.sysdevice_instance = []
        self.process_instance = []
        self.database_instance = []
        self.zone_instance = []

    def _set_sysdevice_instance(self):
        try:
            self.sysdevice_instance = self.model_instance.sysdevice_set.all()
        except Exception:
            self.sysdevice_instance = []

    def _set_zone_instance(self):
        try:
            self.zone_instance = self.model_instance.itsystem_set.all()
        except Exception:
            self.zone_instance = []

    def get_list_related(self):
        return {
        }

    def get_detail_related(self):
        return {
        }

    def get_related_related(self):
        self._set_sysdevice_instance()
        self._set_zone_instance()
        return {
            'sysdevice_list': self.sysdevice_instance, 'sysdevice_count': self.sysdevice_instance.count(),
            'zone_list': self.zone_instance, 'zone_count': self.zone_instance.count(),

        }

    def get_alarm_related(self):
        pass

    def get_record_related(self):
        pass
