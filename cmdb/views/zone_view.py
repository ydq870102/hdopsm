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
from utils.content_params import format_content_dict




@csrf_exempt
def zone_import_view(request):
    data_list = ImportAction(request).parse_data()
    sql_params = sql_import_params(data_list)
    msg = api_action('zone.imp', sql_params)
    if msg or msg is None:
        return JsonResponse(data=msg, status=500, safe=False)
    else:
        return JsonResponse(data=msg, status=200, safe=False)


@csrf_exempt
def zone_list_view(request):
    """
    @ 信息系统页面
    :param request:
    :return: html
    """
    if request.method == 'GET':
        sql_params = sql_get_params(request)
        content_params = {}
        object_list = api_action('zone.get', sql_params)
        object_list, p, objects, page_range, current_page, show_first, show_end = pages(object_list)
        content_params = format_content_dict(content_params, object_list, p, objects, page_range, current_page,
                                             show_first, show_end)
        return render_to_response('cmdb/zone_list.html', content_params)


@csrf_exempt
def zone_search_view(request):
    """
    @ 信息系统页面
    :param request:
    :return: html
    """
    if request.method == 'POST':
        sql_params = sql_search_params(request)
        object_list = api_action('zone.search', sql_params)
        object_list, p, objects, page_range, current_page, show_first, show_end = pages(object_list,
                                                                                        sql_params['current_page'])
        result = list(objects)
        content_html = render_to_string('page.html', locals())
        return JsonResponse(data={'result': result, 'content_html': content_html}, status=200, safe=False)


@csrf_exempt
def zone_delete_view(request):
    if request.method == 'POST':
        sql_params = sql_delete_params(request)
        msg = api_action('zone.delete', sql_params)
        if msg or msg is None:
            return JsonResponse(data=msg, status=500, safe=False)
        else:
            return JsonResponse(data=msg, status=200, safe=False)


def zone_detail_view(request, id):
    if request.is_ajax():
        sql_params = sql_detail_params(id)
        object = api_action('zone.get', sql_params)
        params = {}
        params['object'] = object[0]
        content_html = render_to_string('cmdb/zone_detail.html', params)
        render_dict = {'content_html': content_html}
        return JsonResponse(data=render_dict, status=200, safe=False)


@csrf_exempt
def zone_update_view(request, id):
    if request.is_ajax():
        sql_params = sql_update_params(request, id)
        msg = api_action('zone.update', sql_params)
        if msg or msg is None:
            return JsonResponse(data=msg, status=500, safe=False)
        else:
            return JsonResponse(data=msg, status=200, safe=False)


def zone_template_view(request):
    file = open('static/excel/template_zone.xls', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="template_zone.xls"'
    return response


def zone_export_view(request):
    sql_params = sql_get_params(request)
    object_list = api_action('zone.exp', sql_params)
    export_file, export_file_name = ExportAction(object_list, 'template_zone.xls').parse_data()
    file = open(export_file, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(export_file_name)
    return response
