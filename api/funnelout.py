#! /usr/bin/env python
#  encoding: utf-8

from hdopsm.models import Enum


class FunnelOut(object):

    def __init__(self, model=None, kwargs={}):
        self.model = model
        self.result = kwargs
        self.enum = []
        self.foreignkey = []
        self.querysets = []

    def get_enum_column(self):
        self.enum = Enum.objects.filter(table_name=self.model.__name__).values_list('table_name',
                                                                                    'table_column').distinct()

    def get_foreignkey_column(self):
        if hasattr(self.model,'get_model_foreignkey'):
            self.foreignkey = self.model.get_model_foreignkey()

    def object_to_foreignkey(self):
        for queryset in self.result:
            for key in self.foreignkey:
                for k, v in key.items():
                    queryset[k + '_id'] = v.objects.get(id=queryset[k + '_id']).label_cn
            self.querysets.append(queryset)

    def convert(self):
        self.get_enum_column()
        self.get_foreignkey_column()
        self.object_to_foreignkey()
        if self.querysets:
            return self.querysets
        else:
            return self.result


