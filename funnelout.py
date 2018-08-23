#! /usr/bin/env python
#  encoding: utf-8

from hdopsm.models import Enum


class FunnelOut(object):

    def __init__(self, model=None, kwargs={}):
        self.model = model
        self.result = kwargs
        self.enum = []
        self.foreignkey = []

    def get_enum_column(self):
        self.enum = Enum.objects.filter(table_name=self.model.__name__).values_list('table_name',
                                                                                    'table_column').distinct()

    def get_foreignkey_column(self):
        self.foreignkey = self.model.get_model_foreignkey()

    def object_to_foreignkey(self):
        for key in self.foreignkey:
            for k, v in key.items():
                self.result[k] = v.objects.get(id=self.result[k]).__str__

    def convert(self):
        self.get_enum_column()
        self.get_foreignkey_column()
        self.object_to_foreignkey()
        return self.result
