# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Line(models.Model):
    line_type_choices = (
        ('0', u''),
        ('1', u'电信'),
        ('2', u'移动'),
        ('3', u'内网联通'),
        ('4', u'阿里云'),
        ('5', u'腾讯云'),
    )

    class Meta:
        db_table = 't_com_line'
        verbose_name = '出口线路资产表'
        verbose_name_plural = '出口线路资产表'


class Room(models.Model):
    """
    机房资产
    """
    room_name = models.CharField(max_length=100, unique=True, verbose_name='机房名称')
    room_contact = models.CharField(max_length=100, blank=True, null=True, verbose_name='机房联系人', default='')
    room_phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='联系人号码', default='')
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


class Zone(models.Model):
    """
    放置区域资产
    """
    label_cn = models.CharField(max_length=100, unique=True, verbose_name='网络区域')
    vlan = models.CharField(max_length=100, null=True, verbose_name='vlan', default='')
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    '''自定义权限'''

    class Meta:
        db_table = 't_com_zone'
        permissions = (
            ("can_read_zone_assets", "读取放置区域资产权限"),
            ("can_change_zone_assetss", "更改放置区域资产权限"),
            ("can_add_zone_assets", "添加放置区域资产权限"),
            ("can_delete_zone_assets", "删除放置区域资产权限"),
        )
        verbose_name = '放置区域资产表'
        verbose_name_plural = '放置区域资产表'


class ItSystem(models.Model):
    """
    信息系统资产表
    """
    bool_type_choices = (
        ('0', u'否'),
        ('1', u'是'),
    )
    zone = models.CharField(max_length=100, null=True, verbose_name='所属区域', default='')
    label_cn = models.CharField(max_length=100, null=True, unique=True, verbose_name='信息系统名称')
    use_for = models.CharField(max_length=255, null=True, verbose_name='用途', default='')
    system_framework = models.CharField(max_length=100, null=True, verbose_name='架构描述', default='')
    system_manager = models.CharField(max_length=100, null=True, verbose_name='业务系统管理员', default='')
    system_admin = models.CharField(max_length=100, null=True, verbose_name='业务系统负责人', default='')
    interface_system = models.CharField(max_length=200, null=True, verbose_name='交互系统', default='')
    user_of_service = models.CharField(max_length=200, null=True, verbose_name='使用人员', default='')
    is_untrained_person_use = models.CharField(choices=((u'否', u'否'), ('是', '是')), max_length=20, null=True,
                                               verbose_name='是否普通用户使用', default='')
    line = models.IntegerField(choices=Line.line_type_choices, default=0, null=True, verbose_name='出口线路')
    is_delete = models.IntegerField(choices=bool_type_choices, default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    @staticmethod
    def get_enum_column():
        return [{'ItSystem': 'is_untrained_person_use'}]

    class Meta:
        db_table = 't_com_itsystem'
        permissions = (
            ("can_read_itsystem_assets", "读取信息系统资产权限"),
            ("can_change_itsystem_assets", "更改信息系统资产权限"),
            ("can_add_itsystem_assets", "添加信息系统资产权限"),
            ("can_delete_itsystem_assets", "删除信息系统资产权限"),
        )
        verbose_name = '信息系统资产表'
        verbose_name_plural = '信息系统资产表'


class Host(models.Model):
    assets_type_choices = (
        ('物理机', u'物理机'),
        ('虚拟机', u'虚拟机'),
    )
    # 基础属性
    label_cn = models.CharField(max_length=100, verbose_name='资产编号', unique=True)
    sn = models.CharField(max_length=100, verbose_name='设备序列号', null=True, default='')
    zone = models.CharField(max_length=20, null=True, verbose_name='所属区域', default='')
    itsystem = models.CharField(max_length=100, null=True, verbose_name='信息系统', default='')
    assets_type = models.CharField(choices=assets_type_choices, max_length=100, default='物理机', verbose_name='资产类型')
    status = models.CharField(max_length=20, null=True, verbose_name='状态', default='')
    ip = models.CharField(max_length=100, unique=True, null=True, verbose_name='IP地址', default='')
    management_ip = models.GenericIPAddressField(u'管理IP', null=True, default='')
    use_for = models.CharField(max_length=100, null=True, verbose_name='用途', default='')
    room = models.CharField(max_length=50, null=True, verbose_name='所属机房', default='')
    department = models.CharField(max_length=50, null=True, verbose_name='所属部门', default='')
    host_admin = models.CharField(max_length=30, null=True, verbose_name='系统维护人', default='')
    backup_admin = models.CharField(max_length=30, null=True, verbose_name='备份维护人', default='')
    related_phy_host = models.GenericIPAddressField(u'所属物理机IP', null=True, default='')

    # 配置属性
    hostname = models.CharField(max_length=100, null=True, verbose_name='主机名称', default='')
    username = models.CharField(max_length=100, null=True, verbose_name='用户名', default='')
    passwd = models.CharField(max_length=100, null=True, verbose_name='密码', default='')
    keyfile = models.CharField(max_length=30, null=True, verbose_name='SSH秘钥', default='')
    port = models.DecimalField(max_digits=6, decimal_places=0, null=True, verbose_name='SSH端口', default='')
    line = models.CharField(max_length=30, blank=True, null=True, verbose_name='出口线路', default='')
    mac = models.CharField(max_length=3, null=True, verbose_name='MAC地址', default='')
    cpu = models.CharField(max_length=100, null=True, verbose_name='CPU型号', default='')
    cpu_number = models.SmallIntegerField(blank=True, null=True, verbose_name='CPU个数', default='')
    vcpu_number = models.SmallIntegerField(blank=True, null=True, verbose_name='虚拟CPU个数', default='')
    cpu_core = models.SmallIntegerField(blank=True, null=True, verbose_name='CPU核数', default='')
    disk_total = models.CharField(max_length=100, null=True, verbose_name='硬盘总量', default='')
    ram_total = models.IntegerField(blank=True, null=True, verbose_name='内存总量', default='')
    kernel = models.CharField(max_length=100, null=True, verbose_name='内核版本', default='')
    selinux = models.CharField(max_length=100, null=True, verbose_name='是否开启selinux', default='')
    swap = models.CharField(max_length=100, null=True, verbose_name='swap空间', default='')
    system = models.CharField(max_length=100, null=True, verbose_name='操作系统类型', default='')
    system_version = models.CharField(max_length=100, null=True, verbose_name='操作系统版本', default='')

    # 资产属性
    buy_time = models.DateTimeField(blank=True, null=True, verbose_name='购买时间', default='')
    expire_date = models.DateTimeField(u'过保修期', null=True, default='')
    buy_user = models.CharField(max_length=100, null=True, verbose_name='购买人', default='')
    manufacturer = models.CharField(max_length=30, null=True, verbose_name='制造商', default='')
    provider = models.CharField(max_length=30, null=True, verbose_name='供货商', default='')
    model = models.CharField(max_length=20, null=True, verbose_name='资产型号', default='')

    # 维护属性
    agent_status = models.CharField(max_length=20, null=True, verbose_name='agent状态')
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 't_com_host'
        permissions = (
            ("can_read_host", "读取服务器资产权限"),
            ("can_change_host", "更改服务器资产权限"),
            ("can_add_host", "添加服务器资产权限"),
            ("can_delete_host", "删除服务器资产权限"),
        )
        verbose_name = '服务器表'
        verbose_name_plural = '服务器表'

    @staticmethod
    def get_enum_column():
        return [{'Host': 'assets_type'}, {'Host': 'status'}]
