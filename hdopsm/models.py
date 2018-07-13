#!/usr/bin/env python
# _#_ coding:utf-8 _*_
from django.db import models
import sys




class Department(models.Model):
    """
    部门资产表
    """
    department_name = models.CharField(max_length=100,unique=True,verbose_name='部门名称')
    create_time = models.DateField(auto_now=True)
    last_modify_time = models.DateField(auto_now_add=True)
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
    phone = models.IntegerField(max_length=11,verbose_name='联系电话')
    email = models.EmailField(verbose_name='邮箱')
    department_name = models.ForeignKey('Department_Assets',related_name='department_name',verbose_name='所属部门')
    create_time = models.DateField(auto_now=True)
    last_modify_time = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 't_com_person'
        permissions = (
            ("can_read_person_assets", "读取人员资产权限"),
            ("can_change_person_assets", "更改人员资产权限"),
            ("can_add_person_assets", "添加人员资产权限"),
            ("can_delete_person_assets", "删除人员资产权限"),
        )
        unique_together = (("project", "service_name"))
        verbose_name = '信息系统资产表'
        verbose_name_plural = '信息系统资产表'


class Itsystem(models.Model):
    """
    信息系统资产表
    """
    Department = models.ForeignKey('Department_Assets', related_name='department_name', on_delete=models.SET_DEFAULT,verbose_name='所属部门')
    itsystem_name = models.CharField(max_length=100,verbose_name='信息系统名称')
    use_for = models.CharField(max_length=255,verbose_name='用途')
    system_framework = models.CharField(max_length=100,verbose_name='架构描述')
    system_manager = models.ForeignKey('Person',related_name='person_name',verbose_name='业务系统管理员')
    system_admin = models.ForeignKey('Person',related_name='person_name',verbose_name='业务系统负责人')
    create_time = models.DateField(auto_now=True)
    last_modify_time = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 't_com_itsystem'
        permissions = (
            ("can_read_itsystem_assets", "读取信息系统资产权限"),
            ("can_change_itsystem_assets", "更改信息系统资产权限"),
            ("can_add_itsystem_assets", "添加信息系统资产权限"),
            ("can_delete_itsystem_assets", "删除信息系统资产权限"),
        )
        unique_together = (("project", "service_name"))
        verbose_name = '信息系统资产表'
        verbose_name_plural = '信息系统资产表'


class Room(models.Model):
    """
    机房资产
    """
    room_name = models.CharField(max_length=100,unique=True,verbose_name='机房名称')
    room_contact = models.CharField(max_length=100,blank=True,null=True,verbose_name='机房联系人')
    room_phone = models.CharField(max_length=100,blank=True,null=True,verbose_name='联系人号码')
    create_time = models.DateField(auto_now=True)
    last_modify_time = models.DateField(auto_now_add=True)
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
    line_name = models.CharField(max_length=100, unique=True,verbose_name='网络区域')
    VLAN = models.CharField(max_length=100,verbose_name='VLAN')
    create_time = models.DateField(auto_now=True)
    last_modify_time = models.DateField(auto_now_add=True)
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



class Line(models.Model):
    line_name = models.CharField(max_length=100, unique=True,verbose_name='出口线路名称')
    create_time = models.DateField(auto_now=True)
    last_modify_time = models.DateField(auto_now_add=True)
    '''自定义权限'''

    class Meta:
        db_table = 't_com_line'
        permissions = (
            ("can_read_line_assets", "读取出口线路资产权限"),
            ("can_change_line_assetss", "更改出口线路资产权限"),
            ("can_add_line_assets", "添加出口线路资产权限"),
            ("can_delete_line_assets", "删除出口线路资产权限"),
        )
        verbose_name = '出口线路资产表'
        verbose_name_plural = '出口线路资产表'



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


class Assets(models.Model):
    assets_type_choices = (
                          ('server',u'服务器'),
                          ('vmser',u'虚拟机'),
                          ('switch',u'交换机'),
                          ('route',u'路由器'),
                          ('printer',u'打印机'),
                          ('scanner',u'扫描仪'),
                          ('firewall',u'防火墙'),
                          ('storage',u'存储设备'),
                          ('wifi',u'无线设备'),
                          ('safe', u'安全设备'),
    )
    assets_type = models.CharField(choices=assets_type_choices,max_length=100,default='server',verbose_name='资产类型')
    name = models.CharField(max_length=100,verbose_name='资产编号',unique=True)
    sn =  models.CharField(max_length=100,verbose_name='设备序列号',blank=True,null=True)
    buy_time = models.DateField(blank=True,null=True,verbose_name='购买时间')
    expire_date = models.DateField(u'过保修期',null=True, blank=True)
    buy_user = models.SmallIntegerField(blank=True,null=True,verbose_name='购买人')
    management_ip = models.GenericIPAddressField(u'管理IP',blank=True,null=True)
    manufacturer = models.CharField(max_length=100,blank=True,null=True,verbose_name='制造商')
    provider = models.CharField(max_length=100,blank=True,null=True,verbose_name='供货商')
    model = models.CharField(max_length=100,blank=True,null=True,verbose_name='资产型号')
    status = models.SmallIntegerField(blank=True,null=True,verbose_name='状态')
    room = models.SmallIntegerField(blank=True,null=True,verbose_name='所属机房')
    put_zone = models.SmallIntegerField(blank=True,null=True,verbose_name='放置区域')
    itsystem = models.SmallIntegerField(blank=True,null=True,verbose_name='信息系统')
    department = models.SmallIntegerField(blank=True,null=True,verbose_name='所属部门')
    create_date = models.DateTimeField(auto_now=True)
    last_modify_time = models.DateTimeField(auto_now_add=True)
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
    ip = models.CharField(max_length=100, unique=True, blank=True, null=True,verbose_name='IP地址')
    hostname = models.CharField(max_length=100, blank=True, null=True,verbose_name='主机名称')
    username = models.CharField(max_length=100, blank=True, null=True,verbose_name='用户名')
    passwd = models.CharField(max_length=100, blank=True, null=True,verbose_name='密码')
    keyfile = models.SmallIntegerField(blank=True,null=True,verbose_name='SSH秘钥')  # FileField(upload_to = './upload/key/',blank=True,null=True,verbose_name='密钥文件')
    port = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True,verbose_name='SSH端口')
    line = models.SmallIntegerField(blank=True, null=True,verbose_name='出口线路')
    cpu = models.CharField(max_length=100, blank=True, null=True,verbose_name='CPU型号')
    cpu_number = models.SmallIntegerField(blank=True, null=True,verbose_name='CPU个数')
    vcpu_number = models.SmallIntegerField(blank=True, null=True,verbose_name='虚拟CPU个数')
    cpu_core = models.SmallIntegerField(blank=True, null=True,verbose_name='CPU核数')
    disk_total = models.CharField(max_length=100, blank=True, null=True,verbose_name='硬盘总量')
    ram_total = models.IntegerField(blank=True, null=True,verbose_name='内存总量')
    kernel = models.CharField(max_length=100, blank=True, null=True,verbose_name='内核版本')
    selinux = models.CharField(max_length=100, blank=True, null=True,verbose_name='是否开启selinux')
    swap = models.CharField(max_length=100, blank=True, null=True,verbose_name='虚拟CPU个数')
    raid = models.SmallIntegerField(blank=True, null=True,verbose_name='raid类型')
    system = models.CharField(max_length=100, blank=True, null=True,verbose_name='操作系统类型')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
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


class Network_Assets(models.Model):
    assets = models.OneToOneField('Assets')
    bandwidth = models.CharField(max_length=100, blank=True, null=True, verbose_name='背板带宽')
    ip = models.CharField(max_length=100, blank=True, null=True, verbose_name='管理ip')
    port_number = models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')
    firmware = models.CharField(max_length=100, blank=True, null=True, verbose_name='固件版本')
    cpu = models.CharField(max_length=100, blank=True, null=True, verbose_name='cpu型号')
    stone = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存大小')
    configure_detail = models.TextField(max_length=100, blank=True, null=True, verbose_name='配置说明')
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
        unique_together = (("assets", "device_slot"))
        verbose_name = '磁盘资产表'
        verbose_name_plural = '磁盘资产表'


class Ram_Assets(models.Model):
    assets = models.ForeignKey('Assets')
    device_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存型号')
    device_volume = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存容量')
    device_brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存生产商')
    device_slot = models.SmallIntegerField(blank=True, null=True, verbose_name='内存插槽')
    device_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存状态')
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
        unique_together = (("assets", "device_slot"))
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

    class Meta:
        db_table = 't_assets_networkcard'
        verbose_name = '服务器网卡资产表'
        verbose_name_plural = '服务器网卡资产表'
        unique_together = (("assets", "macaddress"))