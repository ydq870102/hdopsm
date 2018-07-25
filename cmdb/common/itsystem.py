#!/usr/bin/env python
# encoding: utf-8

from cmdb.models import ItSystem


class ItSystemDAO(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_count(self):
        return ItSystem.objects.filter(itsystem_name=self.kwargs.get('itsystem_name')).count()

    def data_format(self):
        self.kwargs['is_delete'] = 0
        iupu = self.kwargs.get('is_untrained_person_use')
        if iupu == '' or iupu == u'否':
            self.kwargs['is_untrained_person_use'] = 0
        elif iupu == u'是':
            self.kwargs['is_untrained_person_use'] = 1
        else:
            self.error_msg('[是否普通用户使用]枚举有误，请填写正确枚举！ ')

    def data_vaild(self):
        pass

    def create(self):
        try:
            ItSystem.objects.create(**self.kwargs)
        except Exception, ex:
            print ex

    @staticmethod
    def delete(id):
        try:
            ItSystem.objects.filter(id=id).update(is_delete=1)
        except Exception, ex:
            print ex

    def update(self):
        try:
            ItSystem.objects.filter(itsystem_name=self.kwargs.get('itsystem_name')).update(**self.kwargs)
        except Exception, ex:
            print ex

    def error_msg(self, msg):
        return msg
