#!/usr/bin/env python
# _#_ coding:utf-8 _*_
from django.db import models
import sys




class Department(models.Model):
    """
    部门资产表
    """
    department_name = models.CharField(max_length=100,unique=True,verbose_name='部门名称')
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
    person_name = models.CharField(max_length=20,unique=True,verbose_name='人员名称')
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


class Room(models.Model):
    """
    机房资产
    """
    room_name = models.CharField(max_length=100,unique=True,verbose_name='机房名称')
    room_contact = models.CharField(max_length=100,blank=True,null=True,verbose_name='机房联系人')
    room_phone = models.CharField(max_length=100,blank=True,null=True,verbose_name='联系人号码')
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    '''自定义权限'''
    class Meta:
        db_table = 't_com_room'
        permissions = (
            ("can_read_room_assets", "读取机房资产权限"),
            ("can_change_room_assets", "更改机房资产权限"),
            ("can_add_room_assets", "添加机房资产权限"),
            ("can_delete_room_assets", "删除机房资产权限"),
        )
        verbose_name = '机房资产表'
        verbose_name_plural = '机房资产表'


class Enum(models.Model):
    """
    枚举表
    """
    table_name = models.CharField(max_length=50, default='', verbose_name='表名')
    table_column = models.CharField(max_length=50, default='', verbose_name='字段名称')
    value  = models.CharField(max_length=100, default='', verbose_name='字段值')
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

"""
class Operate_log(models.Model):
    assets_id = models.IntegerField(verbose_name='资产类型id',blank=True,null=True,default=None)
    assets_user = models.CharField(max_length=50,verbose_name='操作用户',default=None)
    assets_content = models.CharField(max_length=100,verbose_name='名称',default=None)
    assets_type = models.CharField(max_length=50,default=None)
    create_time = models.DateTimeField(auto_now=True,blank=True,null=True,verbose_name='执行时间')
    class Meta:
        db_table = 't_com_log'
        verbose_name = '项目配置操作记录表'
        verbose_name_plural = '项目配置操作记录表'






class Network_Assets(models.Model):
    assets = models.OneToOneField('Assets')
    bandwidth = models.CharField(max_length=100, blank=True, null=True, verbose_name='背板带宽')
    ip = models.CharField(max_length=100, blank=True, null=True, verbose_name='管理ip')
    port_number = models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')
    firmware = models.CharField(max_length=100, blank=True, null=True, verbose_name='固件版本')
    cpu = models.CharField(max_length=100, blank=True, null=True, verbose_name='cpu型号')
    stone = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存大小')
    configure_detail = models.TextField(max_length=100, blank=True, null=True, verbose_name='配置说明')
    is_delete = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_assets_network'
        permissions = (
            ("can_read_network_assets", "读取网络资产权限"),
            ("can_change_network_assets", "更改网络资产权限"),
            ("can_add_network_assets", "添加网络资产权限"),
            ("can_delete_network_assets", "删除网络资产权限"),
        )
        verbose_name = '网络资产表'
        verbose_name_plural = '网络资产表'


class Disk_Assets(models.Model):
    assets = models.ForeignKey('Assets')
    device_volume = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘容量')
    device_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘状态')
    device_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘型号')
    device_brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘生产商')
    device_serial = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘序列号')
    device_slot = models.SmallIntegerField(blank=True, null=True, verbose_name='硬盘插槽')
    is_delete = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_assets_disk'
        permissions = (
            ("can_read_disk_assets", "读取磁盘资产权限"),
            ("can_change_disk_assets", "更改磁盘资产权限"),
            ("can_add_disk_assets", "添加磁盘资产权限"),
            ("can_delete_disk_assets", "删除磁盘资产权限"),
        )
        verbose_name = '磁盘资产表'
        verbose_name_plural = '磁盘资产表'


class Ram_Assets(models.Model):
    assets = models.ForeignKey('Assets')
    device_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存型号')
    device_volume = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存容量')
    device_brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存生产商')
    device_slot = models.SmallIntegerField(blank=True, null=True, verbose_name='内存插槽')
    device_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存状态')
    is_delete = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_assets_ram'
        permissions = (
            ("can_read_ram_assets", "读取内存资产权限"),
            ("can_change_ram_assets", "更改内存资产权限"),
            ("can_add_ram_assets", "添加内存资产权限"),
            ("can_delete_ram_assets", "删除内存资产权限"),
        )
        verbose_name = '内存资产表'
        verbose_name_plural = '内存资产表'


class NetworkCard_Assets(models.Model):
    assets = models.ForeignKey('Assets')
    device = models.CharField(max_length=20, blank=True, null=True)
    macaddress = models.CharField(u'MAC', max_length=64, blank=True, null=True)
    ip = models.GenericIPAddressField(u'IP', blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    mtu = models.CharField(max_length=50, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True, verbose_name='是否在线')
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = 't_assets_networkcard'
        verbose_name = '服务器网卡资产表'
        verbose_name_plural = '服务器网卡资产表'
"""
