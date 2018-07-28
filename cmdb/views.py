#!/usr/bin/env python
# encoding: utf-8


from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from hdopsm.common import pages
from utils.importaction import ImportAction
from utils.apiaction import api_action
from utils.sql_params import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def itsystem_import_view(request):
    data_list = ImportAction(request).parse_data()
    print type(data_list)
    sql_params = sql_import_params(data_list)
    msg = api_action('itsystem.imp', sql_params)
    print msg
    return HttpResponseRedirect('/cmdb/itsystem/list/')


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
        return render_to_response('cmdb/itsystem_list.html', locals())


@csrf_exempt
def itsystem_delete_view(request):
    if request.method == 'POST':
        sql_params = sql_delete_params(request)
        msg = api_action('itsystem.delete', sql_params)
        if msg or msg is None:
            return JsonResponse(json.dumps({'error': msg, 'code': 500}))
        else:
            return JsonResponse({'msg': "删除成功", 'code': 200})
