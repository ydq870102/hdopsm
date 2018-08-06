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


class Zone(models.Model):
    """
    放置区域资产
    """
    line_name = models.CharField(max_length=100, unique=True, verbose_name='网络区域')
    vlan = models.CharField(max_length=100, null=True, verbose_name='vlan')
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateField(auto_now_add=True, null=True)
    last_modify_time = models.DateField(auto_now=True, null=True)
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

    itsystem_name = models.CharField(max_length=100, null=True, unique=True, verbose_name='信息系统名称')
    use_for = models.CharField(max_length=255, null=True, verbose_name='用途')
    system_framework = models.CharField(max_length=100, null=True, verbose_name='架构描述')
    system_manager = models.CharField(max_length=100, null=True, verbose_name='业务系统管理员')
    system_admin = models.CharField(max_length=100, null=True, verbose_name='业务系统负责人')
    interface_system = models.CharField(max_length=200, null=True, verbose_name='交互系统')
    user_of_service = models.CharField(max_length=200, null=True, verbose_name='使用人员')
    is_untrained_person_use = models.CharField(choices=((u'否', u'否'), ('是', '是')), max_length=20, null=True,
                                               verbose_name= '是否普通用户使用')
    line = models.IntegerField(choices=Line.line_type_choices, default=0, null=True, verbose_name='出口线路')
    is_delete = models.IntegerField(choices=bool_type_choices, default=0, null=True)
    create_time = models.DateField(auto_now_add=True, null=True)
    last_modify_time = models.DateField(auto_now=True, null=True)
    zone = models.ForeignKey(Zone)

    @staticmethod
    def get_foreignkey_column():
        return [{'Zone': 'zone'}]

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


class Assets(models.Model):
    assets_type_choices = (
        ('server', u'服务器'),
        ('vmser', u'虚拟机'),
        ('switch', u'交换机'),
        ('route', u'路由器'),
        ('printer', u'打印机'),
        ('scanner', u'扫描仪'),
        ('firewall', u'防火墙'),
        ('storage', u'存储设备'),
        ('wifi', u'无线设备'),
        ('safe', u'安全设备'),
    )
    assets_type = models.CharField(choices=assets_type_choices, max_length=100, default='server', verbose_name='资产类型')
    name = models.CharField(max_length=100, verbose_name='资产编号', unique=True)
    sn = models.CharField(max_length=100, verbose_name='设备序列号', blank=True, null=True)
    buy_time = models.DateField(blank=True, null=True, verbose_name='购买时间')
    expire_date = models.DateField(u'过保修期', null=True, blank=True)
    buy_user = models.SmallIntegerField(blank=True, null=True, verbose_name='购买人')
    management_ip = models.GenericIPAddressField(u'管理IP', blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True, verbose_name='制造商')
    provider = models.CharField(max_length=100, blank=True, null=True, verbose_name='供货商')
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name='资产型号')
    status = models.SmallIntegerField(blank=True, null=True, verbose_name='状态')
    room = models.SmallIntegerField(blank=True, null=True, verbose_name='所属机房')
    department = models.SmallIntegerField(blank=True, null=True, verbose_name='所属部门')
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateField(auto_now_add=True, null=True)
    last_modify_time = models.DateField(auto_now=True, null=True)

    put_zone = models.ForeignKey(Zone)
    itsystem = models.ForeignKey(ItSystem)

    class Meta:
        db_table = 't_com_assets'
        permissions = (
            ("can_read_assets", "读取资产权限"),
            ("can_change_assets", "更改资产权限"),
            ("can_add_assets", "添加资产权限"),
            ("can_delete_assets", "删除资产权限"),
        )
        verbose_name = '总资产表'
        verbose_name_plural = '总资产表'


class Server_Assets(models.Model):
    assets = models.OneToOneField('Assets')
    ip = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name='IP地址')
    hostname = models.CharField(max_length=100, blank=True, null=True, verbose_name='主机名称')
    username = models.CharField(max_length=100, blank=True, null=True, verbose_name='用户名')
    passwd = models.CharField(max_length=100, blank=True, null=True, verbose_name='密码')
    keyfile = models.SmallIntegerField(blank=True, null=True, verbose_name='SSH秘钥')
    port = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True, verbose_name='SSH端口')
    line = models.SmallIntegerField(blank=True, null=True, verbose_name='出口线路')
    cpu = models.CharField(max_length=100, blank=True, null=True, verbose_name='CPU型号')
    cpu_number = models.SmallIntegerField(blank=True, null=True, verbose_name='CPU个数')
    vcpu_number = models.SmallIntegerField(blank=True, null=True, verbose_name='虚拟CPU个数')
    cpu_core = models.SmallIntegerField(blank=True, null=True, verbose_name='CPU核数')
    disk_total = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘总量')
    ram_total = models.IntegerField(blank=True, null=True, verbose_name='内存总量')
    kernel = models.CharField(max_length=100, blank=True, null=True, verbose_name='内核版本')
    selinux = models.CharField(max_length=100, blank=True, null=True, verbose_name='是否开启selinux')
    swap = models.CharField(max_length=100, blank=True, null=True, verbose_name='虚拟CPU个数')
    raid = models.SmallIntegerField(blank=True, null=True, verbose_name='raid类型')
    system = models.CharField(max_length=100, blank=True, null=True, verbose_name='操作系统类型')
    is_delete = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True, null=True)
    last_modify_time = models.DateField(auto_now=True, null=True)
    '''自定义添加只读权限-系统自带了add change delete三种权限'''

    class Meta:
        db_table = 't_assets_server'
        permissions = (
            ("can_read_server_assets", "读取服务器资产权限"),
            ("can_change_server_assets", "更改服务器资产权限"),
            ("can_add_server_assets", "添加服务器资产权限"),
            ("can_delete_server_assets", "删除服务器资产权限"),
        )
        verbose_name = '服务器资产表'
        verbose_name_plural = '服务器资产表'
