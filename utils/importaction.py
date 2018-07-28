#!/usr/bin/env python
# encoding: utf-8

import os
import xlrd
import datetime
import logging
logger = logging.getLogger('django.request')


class ImportAction(object):
    def __init__(self, request):
        self.import_file = request.FILES.get('import_file')
        self.upload_file = ''
        self.upload_file_name = self.import_file.name.split('.')[0]+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.xlsx'
        self.data_list = []

    def save_file(self):
        """
        保存上传的文件
        :return:
        """
        if os.path.isdir(os.getcwd() + '/upload/') is not True:
            os.makedirs(os.getcwd() + '/upload/')
        self.upload_file = os.path.join(os.getcwd() + '/upload/', self.upload_file_name)

        fobj = open(self.upload_file, 'wb')
        for chrunk in self.import_file.chunks():
            fobj.write(chrunk)
        fobj.close()

    def parse_data(self):
        self.save_file()
        bk = xlrd.open_workbook(self.upload_file)
        try:
            template = bk.sheet_by_name("template")
            for nr in range(3, template.nrows):
                data_value = {}
                for lc in range(0,template.ncols):
                    data_value[template.cell_value(1, lc)] =template.cell_value(nr, lc)
                self.data_list.append(data_value)
        except Exception, e:
            logger.error(e.message)
        return self.data_list



