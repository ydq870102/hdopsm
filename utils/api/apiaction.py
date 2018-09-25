#! /usr/bin/env python
#  encoding: utf-8


from utils.api.autoload import AutoLoad
import logging
import traceback


logger = logging.getLogger('django')


def api_action(method="", params={}):
    try:
        module, func = method.split('.')
    except ValueError, e:
        logger.error("method传值有误：{}".format(method))
        return False
    at = AutoLoad()
    if not at.is_vaild_module(module):
        logger.error("{} 模块不可用".format(module))
        return False
    if not at.is_vaild_method(func):
        logger.error("{} 函数不可用".format(func))
        return False
    try:
        called = at.get_call_method()
        if callable(called):
            return called(**params)
        else:
            logger.error("函数不能被调用{}.{}".format(module, func))
            return False
    except Exception, e:
        logger.error("调用模块执行中出错：{}".format(traceback.format_exc()))
