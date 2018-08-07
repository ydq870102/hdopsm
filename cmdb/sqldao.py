#!/usr/bin/env python
# encoding: utf-8


from cmdb.models import *
from django.db.models import Count


def get_itsystem_zone():
    zone_list = ItSystem.objects.all().filter(is_delete=0).values('zone').annotate(zone_count=Count('id'))
    data = []
    for item in zone_list:
        temp = {}
        temp['zone'] = item['zone']
        temp['zone_count'] = item['zone_count']
        data.append(temp)
    return data
