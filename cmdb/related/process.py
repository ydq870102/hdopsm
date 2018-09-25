#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
import base


class ProcessRelated(base.BaseRelated):

    def __init__(self, sql_id=''):
        super(ProcessRelated, self).__init__(Process, sql_id)
        self.get_instance()
        self.process_instance = []
        self.database_instance = []

    def get_list_related(self):
        return {
            'process_itsystem_list': base.get_related_foreignkey_count(Process, 'related_itsystem_id_id', ItSystem),
            'process_device_list': base.get_related_foreignkey_count(Process, 'related_device_id_id', SysDevice),
        }

    def get_detail_related(self):
        return {'itsystem_label_list': base.get_related_attr(ItSystem, 'label_cn'),
                'sysdevice_label_list': base.get_related_attr(SysDevice, 'label_cn'),
                'process_crole_enum_list': base.get_related_column_enum('Process', 'cluster_role'),
                }

    def get_related_related(self):
        return {}

    def get_alarm_related(self):
        return {}

    def get_record_related(self):
        return {}
