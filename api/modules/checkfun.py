#! /usr/bin/env python
#  encoding: utf-8


def check_exists_filed(model, kwargs):
    for filed in kwargs.keys():
        if not hasattr(model, filed):
            print "参数错误,{} 不在{}这张表里".format(model, filed)
            raise Exception("params error: {}".format(filed))
        else:
            return True


def check_output_filed(model, output):
    if not isinstance(output, list):
        print "output 必须为list"
        raise Exception("output 必须为list")
    for field in output:
        if not hasattr(model, field):
            print "{} 这个输出字段不存在".format(field)
            raise Exception("{} 这个输出字段不存在".format(field))
    else:
        return True


def check_order_by(model, order_by):
    if not hasattr(model, order_by.replace('-', '').lower()):
        print "排序字段不在表中"
        raise Exception("排序字段不在表中")

    return True


def check_limit_type(limit):
    if str(limit).isdigit() or limit is None:
        return True
    else:
        print "limit 值必须为数字"
        raise Exception("limit 值必须为数字")
