#!/usr/bin/env python
# encoding: utf-8


def sql_get_params(request):
    if request.method == 'GET':
        output = request.GET.get('output', [])
        order_by = request.GET.get('order_by', 'id')
        limit = request.GET.get('limit', None)
        where = request.GET.get('order_by', {})
        where['is_delete'] = 0
        return {"where": where, "output": output, "limit": limit, "order_by": order_by}

    elif request.method == 'POST':
        output = request.GET.get('output', [])
        order_by = request.GET.get('order_by', 'id')
        limit = request.GET.get('limit', None)
        where = request.GET.get('order_by', {})
        where['is_delete'] = 0
        return {"where": where, "output": output, "limit": limit, "order_by": order_by}
