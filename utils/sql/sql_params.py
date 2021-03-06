#!/usr/bin/env python
# encoding: utf-8
import json


def sql_get_params(request):
    """
    @ 对象查询条件拼接
    :param request:
    :return: 条件字典
    """
    if request.method == 'GET':
        output = request.GET.get('output', [])
        order_by = request.GET.get('order_by', 'id')
        limit = request.GET.get('limit', None)
        where = request.GET.get('where', {})
        if isinstance(where, (unicode)):
            where = json.loads(where)
        where['is_delete'] = 0
    elif request.method == 'POST':
        output = request.POST.get('output', [])
        order_by = request.POST.get('order_by', 'id')
        limit = request.POST.get('limit', None)
        where = request.POST.get('where', {})
        if isinstance(where, (unicode)):
            where = json.loads(where)
        where['is_delete'] = 0
    return format_dict(where=where, output=output, limit=limit, order_by=order_by)


def sql_create_params(request):
    """
    @ 对象新增条件拼接
    :param request:
    :return: 条件字典
    """
    if request.method == 'POST':
        result = request.POST.get('result', {})
        return format_dict(result=result)


def sql_delete_params(request):
    """
    @ 对象删除条件拼接
    :param request:
    :return: 条件字典
    """
    if request.method == 'POST':
        if request.POST.getlist('where[]', []):
            where = request.POST.getlist('where[]', [])
        else:
            where = request.POST.get('where', {})
        return format_dict(where=where)


def sql_update_params(request, id=None):
    """
    @ 对象更新条件拼接
    :param request:
    :return: 条件字典
    """
    if request.method == 'POST':
        where = request.POST.get('where', {'id': id})
        result = request.POST.get('result', {})
        return format_dict(where=where, result=result)


def sql_import_params(result):
    """
    @ 对象导入条件拼接
    :param request:
    :return: 条件字典
    """
    return format_dict(result=result)


def sql_detail_params(id):
    """
    @ 对象明细条件拼接
    :param request:
    :return: 条件字典
    """
    return format_dict(where={"id": id})


def sql_search_params(request):
    """
    @ 对象明细条件拼接
    :param request:
    :return: 条件字典
    """
    if request.method == 'POST':
        output = request.POST.get('output', [])
        order_by = request.POST.get('order_by', 'id')
        limit = request.POST.get('limit', None)
        where = request.POST.get('where', {})
        current_page = request.POST.get('current_page', '')
        if isinstance(where, (unicode)):
            where = json.loads(where)
        where['is_delete'] = 0
        return format_dict(where=where, output=output, limit=limit, order_by=order_by, current_page=current_page)


def format_dict(output=[], order_by='id', limit=None, where={}, result={}, current_page= ''):
    """
    @返回结果封装
    :param output:
    :param order_by:
    :param limit:
    :param where:
    :param result:
    :return:
    """
    return {"where": where, "output": output, "limit": limit, "order_by": order_by, "result": result,
            "current_page": current_page}
