# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.


class Room(models.Model):
    """
    @ 机房模型
    """
    # 基础属性
    label_cn = models.CharField(max_length=100, unique=True, verbose_name='机房名称')
    addr = models.CharField(max_length=255, verbose_name='机房地址', null=True)
    room_contact = models.CharField(max_length=100, verbose_name='机房联系人', null=True)
    room_phone = models.CharField(max_length=20, verbose_name='联系人号码', null=True)
    # 维护属性
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True)
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

    def __str__(self):
        return str(self.label_cn)


class Zone(models.Model):
    """
    @ 网络区域模型
    """
    # 基础属性
    label_cn = models.CharField(max_length=100, unique=True, verbose_name='网络区域')
    vlan = models.CharField(max_length=100, verbose_name='vlan', null=True)
    # 维护属性
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True)
    '''自定义权限'''

    class Meta:
        db_table = 't_com_zone'
        permissions = (
            ("can_read_zone_assets", "读取网络区域资产权限"),
            ("can_change_zone_assetss", "更改网络区域资产权限"),
            ("can_add_zone_assets", "添加网络区域资产权限"),
            ("can_delete_zone_assets", "删除网络区域资产权限"),
        )
        verbose_name = '网络区域资产表'
        verbose_name_plural = '网络区域资产表'

    def __str__(self):
        return str(self.label_cn)


class ItSystem(models.Model):
    """
    @ 信息系统模型
    """
    # 基础属性
    label_cn = models.CharField(max_length=100, unique=True, verbose_name='信息系统名称')
    related_zone_id = models.ForeignKey(Zone, db_column='related_zone_id', null=True, )
    use_for = models.CharField(max_length=255, verbose_name='用途', null=True)
    system_framework = models.CharField(max_length=100, verbose_name='架构描述', null=True)
    user_of_service = models.CharField(max_length=200, verbose_name='使用人员', null=True)
    is_untrained_person_use = models.CharField(max_length=20, verbose_name='是否普通用户使用', default='否', null=True)
    access_mode = models.CharField(max_length=200, verbose_name='访问方式', null=True)
    # 维护属性
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True)
    system_manager = models.CharField(max_length=100, verbose_name='业务系统管理员', null=True)
    system_admin = models.CharField(max_length=100, verbose_name='业务系统负责人', null=True)

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

    def __str__(self):
        return str(self.label_cn)

    @staticmethod
    def get_model_foreignkey():
        return [{'related_zone_id': Zone}]


class SysDevice(models.Model):
    """
    @ 服务器模型
    """
    assets_type_choices = (
        ('物理机', u'物理机'),
        ('虚拟机', u'虚拟机'),
    )
    # 基础属性
    label_cn = models.CharField(max_length=100, verbose_name='集团编码', unique=True)
    related_zone_id = models.ForeignKey(Zone, db_column='related_zone_id', verbose_name='所属区域ID')
    related_itsystem_id = models.ForeignKey(ItSystem, db_column='related_itsystem_id', verbose_name='所属信息系统ID')
    related_room_id = models.ForeignKey(Room, db_column='related_room_id', verbose_name='所属机房ID')
    ipaddr = models.GenericIPAddressField(unique=True, verbose_name='IP地址')
    system = models.CharField(max_length=20, default='Linux', verbose_name='操作系统类型')
    management_ip = models.GenericIPAddressField(null=True, verbose_name='管理IP地址')
    assets_type = models.CharField(choices=assets_type_choices, max_length=20, default='物理机', verbose_name='资产类型')
    related_host_ip = models.GenericIPAddressField(null=True, verbose_name='所属物理机IP')
    status = models.CharField(max_length=20, null=True, verbose_name='状态')
    use_for = models.CharField(max_length=100, null=True, verbose_name='用途')
    # 资产属性
    sn = models.CharField(max_length=100, null=True, verbose_name='设备序列号')
    model = models.CharField(max_length=20, null=True, verbose_name='资产型号')
    provider = models.CharField(max_length=30, null=True, verbose_name='供货商')
    buy_user = models.CharField(max_length=100, null=True, verbose_name='购买人')
    manufacturer = models.CharField(max_length=30, null=True, verbose_name='制造商')
    buy_time = models.DateTimeField(null=True, verbose_name='购买日期')
    expire_date = models.DateTimeField(null=True, verbose_name='过保日期')
    # 配置属性
    hostname = models.CharField(max_length=100, null=True, verbose_name='主机名称', default=None)
    mac = models.CharField(max_length=3, null=True, verbose_name='MAC地址', default=None)
    cpu = models.CharField(max_length=100, null=True, verbose_name='CPU型号', default=None)
    cpu_core = models.SmallIntegerField(blank=True, null=True, verbose_name='CPU核数', default=None)
    ram_total = models.IntegerField(blank=True, null=True, verbose_name='内存总量', default=None)
    disk_total = models.CharField(max_length=100, null=True, verbose_name='硬盘总量', default=None)
    system_version = models.CharField(max_length=100, null=True, verbose_name='操作系统版本', default=None)
    # 维护属性
    agent_status = models.CharField(max_length=20, null=True, verbose_name='agent状态')
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    system_admin = models.CharField(max_length=30, null=True, verbose_name='系统维护人', default=None)
    backup_admin = models.CharField(max_length=30, null=True, verbose_name='备份维护人', default=None)

    class Meta:
        db_table = 't_sys_device'
        permissions = (
            ("can_read_device", "读取服务器资产权限"),
            ("can_change_device", "更改服务器资产权限"),
            ("can_add_device", "添加服务器资产权限"),
            ("can_delete_device", "删除服务器资产权限"),
        )
        verbose_name = '服务器表'
        verbose_name_plural = '服务器表'

    # def __str__(self):
    #     return str(self.label_cn)

    @staticmethod
    def get_model_foreignkey():
        return [{'related_zone_id': Zone}, {'related_itsystem_id': ItSystem}, {'related_room_id':Room}]


class Process(models.Model):
    """
    @ 服务器模型
    """
    # 基础属性
    related_itsystem_id = models.ForeignKey(ItSystem, db_column='related_itsystem_id', verbose_name='所属信息系统ID')
    related_device_id = models.ForeignKey(SysDevice, db_column='related_device_id', verbose_name='所属服务器ID')
    label_cn = models.CharField(max_length=20, verbose_name='应用名称', unique=True)
    cluster_name = models.CharField(max_length=20, null=True, verbose_name='集群名称')
    cluster_role = models.CharField(max_length=20, null=True, verbose_name='集群角色')
    dev_language = models.CharField(max_length=20, null=True, verbose_name='开发语言')
    middleware = models.CharField(max_length=100, null=True, verbose_name='中间件')
    path = models.CharField(max_length=100, null=True, verbose_name='部署路径')
    port = models.CharField(max_length=50, null=True, verbose_name='端口')
    use_for = models.CharField(max_length=100, null=True, verbose_name='用途')
    # 维护属性
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True)
    start_command = models.CharField(max_length=100, null=True, verbose_name='启动命令')
    stop_command = models.CharField(max_length=100, null=True, verbose_name='停止命令')
    status = models.CharField(max_length=20, null=True, verbose_name='状态')

    class Meta:
        db_table = 't_sys_process'
        permissions = (
            ("can_read_process", "读取服务器资产权限"),
            ("can_change_process", "更改服务器资产权限"),
            ("can_add_process", "添加服务器资产权限"),
            ("can_delete_process", "删除服务器资产权限"),
        )
        verbose_name = '应用程序表'
        verbose_name_plural = '应用程序表'

    # def __str__(self):
    #     return str(self.label_cn)

    @staticmethod
    def get_model_foreignkey():
        return [{'related_itsystem_id': ItSystem}, {'related_device_id': SysDevice}]


class Database(models.Model):
    """
    @ 服务器模型
    """
    # 基础属性
    label_cn = models.CharField(max_length=20, verbose_name='数据库名称', unique=True)
    cluster_name = models.CharField(max_length=20, null=True, verbose_name='集群名称')
    cluster_role = models.CharField(max_length=20, null=True, verbose_name='集群角色')
    related_itsystem_id = models.ForeignKey(ItSystem, db_column='related_itsystem_id', verbose_name='所属信息系统ID')
    related_device_id = models.ForeignKey(SysDevice, db_column='related_device_id', verbose_name='所属服务器ID')
    database_type = models.CharField(max_length=20, null=True, verbose_name='数据库类型')
    path = models.CharField(max_length=100, null=True, verbose_name='部署路径')
    port = models.CharField(max_length=50, null=True, verbose_name='端口')
    use_for = models.CharField(max_length=100, null=True, verbose_name='用途')
    # 维护属性
    is_delete = models.IntegerField(default=0, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    last_modify_time = models.DateTimeField(auto_now=True, null=True)
    start_command = models.CharField(max_length=100, null=True, verbose_name='启动命令')
    stop_command = models.CharField(max_length=100, null=True, verbose_name='停止命令')
    status = models.CharField(max_length=20, null=True, verbose_name='状态')

    class Meta:
        db_table = 't_sys_database'
        permissions = (
            ("can_read_database", "读取数据库资产权限"),
            ("can_change_database", "更改数据库资产权限"),
            ("can_add_database", "添加数据库资产权限"),
            ("can_delete_database", "删除数据库资产权限"),
        )
        verbose_name = '数据库表'
        verbose_name_plural = '数据库表'

    # def __str__(self):
    #     return str(self.label_cn)

    @staticmethod
    def get_model_foreignkey():
        return [{'related_itsystem_id': ItSystem}, {'related_device_id': SysDevice}]
