#! /usr/bin/env python
#  encoding: utf-8


def get_filter(kwargs={}, eargs={}):
    output = kwargs.get("output", [])
    limit = kwargs.get("limit", None)
    order_by = kwargs.get("order_by", "-id")
    where = kwargs.get("where", {})
    foreignkey = eargs.get('foreignkey', {})
    enum = eargs.get('enum')
    return {'output': output, "limit": limit, 'order_by': order_by, 'where': where,
            'foreignkey': foreignkey, 'enum': enum}