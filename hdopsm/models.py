#!/usr/bin/env python
# _#_ coding:utf-8 _*_

from django.db import models


class Department(models.Model):
    """
    部门资产表
    """
    department_name = models.CharField(max_length=100, unique=True, verbose_name='部门名称')
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 't_com_department'
        permissions = (
            ("can_read_department_assets", "读取部门权限"),
            ("can_change_department_assets", "更改部门权限"),
            ("can_add_department_assets", "添加部门权限"),
            ("can_delete_department_assets", "删除部门权限"),
        )
        verbose_name = '部门资产表'
        verbose_name_plural = '部门资产表'


class Person(models.Model):
    """
    人员资产表
    """
    person_name = models.CharField(max_length=20, unique=True, verbose_name='人员名称')
    phone = models.IntegerField(verbose_name='联系电话', null=True)
    email = models.EmailField(verbose_name='邮箱', null=True)
    department_name = models.CharField(max_length=20, verbose_name='所属部门', null=True)
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 't_com_person'
        permissions = (
            ("can_read_person_assets", "读取人员资产权限"),
            ("can_change_person_assets", "更改人员资产权限"),
            ("can_add_person_assets", "添加人员资产权限"),
            ("can_delete_person_assets", "删除人员资产权限"),
        )
        verbose_name = '信息系统资产表'
        verbose_name_plural = '信息系统资产表'


class Enum(models.Model):
    """
    枚举表
    """
    table_name = models.CharField(max_length=50, default='', verbose_name='表名')
    table_column = models.CharField(max_length=50, default='', verbose_name='字段名称')
    value = models.CharField(max_length=100, default='', verbose_name='字段值')
    value_desc = models.CharField(max_length=100, default='', verbose_name='值描述')
    '''自定义权限'''

    class Meta:
        db_table = 't_com_enum'
        permissions = (
            ("can_read_enum_assets", "读取枚举表权限"),
            ("can_change_enum_assets", "更改枚举表权限"),
            ("can_add_enum_assets", "添加枚举表权限"),
            ("can_delete_enum_assets", "删除枚举表权限"),
        )
        verbose_name = '枚举表'
        verbose_name_plural = '枚举表'
