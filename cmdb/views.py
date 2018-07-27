#!/usr/bin/env python
# encoding: utf-8


from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db.models import Q
from hdopsm.common import pages
from utils.importaction import ImportAction
from utils.apiaction import api_action
from utils.sql_params import *
from django.views.decorators.csrf import csrf_exempt
from common.itsystem import *
from django.http import JsonResponse
import logging

logger = logging.getLogger('info_handler')
@csrf_exempt
def itsystem_import_view(request):
    data_list = ImportAction(request).get_data()
    for data in data_list:
        itsystem = {
            'zone': data[0],
            'itsystem_name': data[1],
            'use_for': data[2],
            'system_framework': data[3],
            'system_manager': data[4],
            'system_admin': data[5],
            'interface_system': data[6],
            'is_untrained_person_use': data[7],
            'user_of_service': data[8],
        }
        itsystemobj = ItSystemDAO(**itsystem)
        itsystemobj.data_format()
        count = itsystemobj.get_count()
        if count == 1:
            itsystemobj.update()
        else:
            itsystemobj.create()
    return HttpResponseRedirect('/cmdb/itsystem/list/')



@csrf_exempt
def itsystem_delete_view(request):
    print request.POST
    keys = request.POST.getlist('ids[]', '')
    for key in keys:
        print key
        ItSystemDAO.delete(key)
    return JsonResponse({'msg': "删除成功", 'code': 200})


@csrf_exempt
def itsystem_list_view(request):
    """
    @ 信息系统页面
    :param request:
    :return: html
    """
    if request.method == 'GET':
        sql_params = sql_get_params(request)
        object_list = api_action('itsystem.get', sql_params)
        object_list, p, objects, page_range, current_page, show_first, show_end = pages(object_list, request)
        print object_list
        return render_to_response('cmdb/itsystem_list.html', locals())
