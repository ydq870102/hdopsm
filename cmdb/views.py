#!/usr/bin/env python
# encoding: utf-8


from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from hdopsm.common import pages
from utils.importaction import ImportAction
from utils.exportaction import ExportAction
from utils.apiaction import api_action
from utils.sql_params import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse
from cmdb.sqldao import *
from django.db.models import Q
from django.core import serializers


@csrf_exempt
def itsystem_import_view(request):
    data_list = ImportAction(request).parse_data()
    sql_params = sql_import_params(data_list)
    msg = api_action('itsystem.imp', sql_params)
    # msg = ",".join(msg)
    if msg or msg is None:
        return JsonResponse(data=msg, status=500, safe=False)
    else:
        return JsonResponse(data=msg, status=200, safe=False)


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
        zones = get_itsystem_zone()
        return render_to_response('cmdb/itsystem_list.html', locals())
    if request.method == 'POST':
        sql_params = sql_get_params(request)
        object_list = api_action('itsystem.get', sql_params)
        object_list, p, objects, page_range, current_page, show_first, show_end = pages(object_list, request)
        result = list(object_list)
        return JsonResponse(data=result, status=200, safe=False)


def itsystem_search_view(request):
    """
    @ 信息系统页面
    :param request:
    :return: html
    """
    if request.method == 'POST':
        sql_params = sql_get_params(request)
        object_list = api_action('itsystem.get', sql_params)
        object_list = ItSystem.objects.filter(Q(**sql_params['where']))
        result = list(object_list)
        return JsonResponse(data=result, status=200, safe=False)


@csrf_exempt
def itsystem_delete_view(request):
    if request.method == 'POST':
        sql_params = sql_delete_params(request)
        msg = api_action('itsystem.delete', sql_params)
        if msg or msg is None:
            return JsonResponse(data=msg, status=500, safe=False)
        else:
            return JsonResponse(data=msg, status=200, safe=False)


def itsystem_detail_view(request, id):
    if request.is_ajax():
        sql_params = sql_detail_params(id)
        object = api_action('itsystem.get', sql_params)
        content_html = render_to_string('cmdb/itsystem_detail.html', {"object": object[0]})
        render_dict = {'content_html': content_html}
        return JsonResponse(data=render_dict, status=200, safe=False)


@csrf_exempt
def itsystem_update_view(request, id):
    if request.is_ajax():
        sql_params = sql_update_params(request, id)
        msg = api_action('itsystem.update', sql_params)
        if msg or msg is None:
            return JsonResponse(data=msg, status=500, safe=False)
        else:
            return JsonResponse(data=msg, status=200, safe=False)


def itsystem_template_view(request):
    file = open('static/excel/template_itsystem.xls', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="template_itsystem.xls"'
    return response


def itsystem_export_view(request):
    sql_params = sql_get_params(request)
    object_list = api_action('itsystem.exp', sql_params)
    export_file, export_file_name = ExportAction(object_list, 'template_itsystem.xls').parse_data()
    file = open(export_file, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(export_file_name)
    return response
