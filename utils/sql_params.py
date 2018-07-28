#!/usr/bin/env python
# encoding: utf-8


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
        where['is_delete'] = 0
        return {"where": where, "output": output, "limit": limit, "order_by": order_by}

    elif request.method == 'POST':
        output = request.POST.get('output', [])
        order_by = request.POST.get('order_by', 'id')
        limit = request.POST.get('limit', None)
        where = request.POST.get('where', {})
        where['is_delete'] = 0
        return {"where": where, "output": output, "limit": limit, "order_by": order_by}


def sql_create_params(request):
    """
    @ 对象新增条件拼接
    :param request:
    :return: 条件字典
    """
    if request.method == 'POST':
        result = request.POST.get('result', {})
        return {"result": result}


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
        return {"where": where}


def sql_update_params(request):
    """
    @ 对象更新条件拼接
    :param request:
    :return: 条件字典
    """
    if request.method == 'POST':
        where = request.POST.get('where', {})
        result = request.POST.get('result', {})
        return {"where": where, "result": result}


def sql_import_params(args):
    """
    @ 对象导入条件拼接
    :param request:
    :return: 条件字典
    """
    print type(args)
    return {"result": args}