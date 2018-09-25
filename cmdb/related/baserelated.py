#!/usr/bin/env python
# encoding: utf-8


from hdopsm.models import Enum
from django.db.models import Count


class BaseRelated(object):

    def __init__(self, model, sql_id):
        self.model = model
        self.sql_id = sql_id
        self.model_instance = None

    def get_instance(self):
        try:
            self.model_instance = self.model.objects.get(id=self.sql_id)
        except Exception,e:
            self.model_instance = None

    def get_list_related(self):
        pass

    def get_detail_related(self):
        pass

    def get_related_related(self):
        pass

    def get_alarm_related(self):
        pass

    def get_record_related(self):
        pass

    @staticmethod
    def __get_related_column_count(model, column):
        """
        @ 对象字段统计
        :param model:
        :param column:
        :return:
        """
        if hasattr(model, column):
            column_list = model.objects.all().filter(is_delete=0).values(column).order_by(column).annotate(
                column_count=Count('id'))
            data = []
            for item in column_list:
                temp = {}
                temp['column'] = item[column]
                temp['column_count'] = item['column_count']
                data.append(temp)
            return data

    @staticmethod
    def __get_related_column_enum(model, column):
        """
        @ 对象字段枚举
        :return:
        """
        column_list = Enum.objects.filter(table_name=model, table_column=column).values('value_desc')
        data = []
        for item in column_list:
            data.append(item['value_desc'])
        return data

    @staticmethod
    def __get_related_foreignkey_count(model, column, foreignkey):
        """
        @ 对象字段枚举
        :return:
        """
        if hasattr(model, column):
            column_list = model.objects.all().filter(is_delete=0).values(column).order_by(column).annotate(
                column_count=Count('id'))
            data = []
            for item in column_list:
                temp = {}
                temp['id'] = item[column]
                temp['column'] = foreignkey.objects.get(id=item[column]).label_cn
                temp['column_count'] = item['column_count']
                data.append(temp)
            return data

    @staticmethod
    def __get_related_attr(model, column):
        """
        下拉框
        :return:
        """
        if hasattr(model, column):
            data_list = model.objects.all().values(column)
            data = []
            for item in data_list:
                data.append(item[column])
            return data


def get_object_column_count(model, column):
    """
    @ 对象字段统计
    :param model:
    :param column:
    :return:
    """
    if hasattr(model, column):
        column_list = model.objects.all().filter(is_delete=0).values(column).order_by(column).annotate(
            column_count=Count('id'))
        data = []
        for item in column_list:
            temp = {}
            temp['column'] = item[column]
            temp['column_count'] = item['column_count']
            data.append(temp)
        return data


def get_object_column_enum(model, column):
    """
    @ 对象字段枚举
    :return:
    """
    column_list = Enum.objects.filter(table_name=model, table_column=column).values('value_desc')
    data = []
    for item in column_list:
        data.append(item['value_desc'])
    return data


def get_object_attr(model, column):
    """
    下拉框
    :return:
    """
    if hasattr(model, column):
        data_list = model.objects.all().values(column)
        data = []
        for item in data_list:
            data.append(item[column])
        return data


def get_object_column_foreignkey_count(model, column, foreignkey):
    """
    @ 对象字段枚举
    :return:
    """
    if hasattr(model, column):
        column_list = model.objects.all().filter(is_delete=0).values(column).order_by(column).annotate(
            column_count=Count('id'))
        data = []
        for item in column_list:
            temp = {}
            temp['id'] = item[column]
            temp['column'] = foreignkey.objects.get(id=item[column]).label_cn
            temp['column_count'] = item['column_count']
            data.append(temp)
        return data
