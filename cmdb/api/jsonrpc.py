#! /usr/bin/env python
#  encoding: utf-8

from autoload import AutoLoad


class JsonRPC(object):

    def __init__(self):
        self.jsonData = None
        self.VERSION = "2.0"
        self._response = {}

    def execute(self):
        if self.jsonData.get("id",None) is None:
            self.jsonError("-1", "102", "id 没有传")
            return self._response
        if self.vaildate():
            params = self.jsonData["params"]
            auth = self.jsonData["auth"]
            module, method = self.jsonData["method"].split(".")
            ret = self.callMethod(module, method, auth, params)
            self.processResult(ret)
        return self._response

    def vail_date(self):
        if self.jsonData is None:
            self.jsonError(self.jsonData["id"], "101", "json 数据为空")
            return False
        for opt in ["jsonrpc",  "method", "params", "auth",]:
            if not self.jsonData.has_key(opt):
                self.jsonError(self.jsonData["id"], "102", "{} 没有传".format(opt))
        if str(self.jsonData["jsonrpc"]) != "2.0":
            self.jsonError(self.jsonData["id"], "103", "jsonrpc版本不正确")
        action = self.jsonData["method"].split('.')
        if len(action) != 2:
            self.jsonError(self.jsonData["id"], "104", "method 错误")
        if not str(self.jsonData["id"]).isdigit():
            self.jsonError(self.jsonData["id"], "105", "ID 必须为数字")
        if not isinstance(self.jsonData["params"],dict):
            self.jsonError(self.jsonData["id"], "106", "params 必须为字典")
        return True

    def json_error(self, id, errno, errmsg):
        self._response = {
            "jsonrpc": self.VERSION,
            "id": id,
            "error_code": errno,
            "errmsg": errmsg
        }

    def require_auth(module_name, method_name):
        white_list = ["user.login", "host.get"]
        if "{}.{}".format(module_name, method_name) in white_list:
            return False
        return False

    def call_method(self, module, method, auth, params):

        module_name = module.lower()
        method_name = method.lower()

        response = Response()
        at = AutoLoad()

        if not at.is_vaild_module(module_name):
            response.errorCode = 107
            response.errorMessage = "模块不存在"
            return response
        if not at.is_vaild_method(method_name):
            response.errorCode = 108
            response.errorMessage = "{}下函数{}不存在".format(method_name, method_name)
            return response
        if self.require_auth(module_name, method_name):
            if auth is None:
                response.errorCode = 109
                response.errorMessage = "该操作需要提供auth"
                return response
        try:
            called = at.get_call_method()
            if callable(called):
                response.data = called(**params)
            else:
                response.errorCode = 109
                response.errorMessage = "模块{}下函数{}执行错误".format(method_name, method_name)
        except Exception,e:
                response.errorCode = -1
                response.errorMessage = e.message
        return response

    def process_result(self, response):

        if response.errorCode != 0:
            self.jsonError(self.jsonData["id"],
                           response.errorCode,
                           response.errorMessage)
        else:
            self._response = {
                "jsonrpc": self.VERSION,
                "id": self.jsonData["id"],
                "result": response.data
            }


class Response(object):

    def __init__(self):
        self.data = None
        self.errorCode = 0
        self.errorMessage = None


if __name__ == "__main__":
    js = JsonRPC()
    js.jsonData ={"jsonrpc": "2.0", "id": "1", "method": "host.get", "auth": "", "params": {}}
    print js.execute()
