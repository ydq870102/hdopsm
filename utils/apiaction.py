#! /usr/bin/env python
#  encoding: utf-8


from api.autoload import AutoLoad


def api_action(method="", params={}):
    try:
        module, func = method.split('.')
    except ValueError, e:
        print "method传值有误：{}".format(method)
        print e.message
        return False
    at = AutoLoad()
    if not at.is_vaild_module(module):
        print "{} 模块不可用".format(module)
        return False
    if not at.is_vaild_method(func):
        print "{} 函数不可用".format(func)
        return False
    try:
        called = at.get_call_method()
        if callable(called):
            return called(**params)
        else:
            print "函数不能被调用{}.{}".format(module, func)
            return False
    except Exception, e:
        print "调用模块执行中出错：{}".format(e.message)
