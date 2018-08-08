#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
from django.db.models import Count
from django.db.models import Q

def get_itsystem_zone():
    zone_list = ItSystem.objects.all().filter(is_delete=0).values('zone').order_by('zone').annotate(
        zone_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['zone'] = item['zone']
        temp['zone_count'] = item['zone_count']
        data.append(temp)
    return data


def get_itsystem_system_manager():
    zone_list = ItSystem.objects.all().filter(is_delete=0).values('system_manager').order_by('system_manager').annotate(
        system_manager_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['system_manager'] = item['system_manager']
        temp['system_manager_count'] = item['system_manager_count']
        data.append(temp)
    return data


def get_itsystem_system_admin():
    zone_list = ItSystem.objects.all().filter(is_delete=0).values('system_admin').order_by('system_admin').annotate(
        system_admin_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['system_admin'] = item['system_admin']
        temp['system_admin_count'] = item['system_admin_count']
        data.append(temp)
    return data

