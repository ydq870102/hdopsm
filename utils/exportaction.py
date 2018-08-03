#!/usr/bin/env python
# encoding: utf-8

import os
import xlrd
import datetime
import logging
import traceback
logger = logging.getLogger('django')


class ExportAction(object):
    def __init__(self, query_set, tempalte_file):
        self.temp_file = ''
        self.template_file = 'static/excel/'+tempalte_file
        self.export_file = ''
        self.query_set = query_set
        # self.upload_file_name = self.import_file.name.split('.')[0]+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.xlsx'

    def create_temp_file(self):
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
            sheet = bk.sheet_by_name("template")
            for nr in range(3, sheet.nrows):
                data_value = {}
                for lc in range(0,sheet.ncols):
                    data_value[sheet.cell_value(1, lc)] =sheet.cell_value(nr, lc)
                self.data_list.append(data_value)
        except Exception, e:
            logger.error(traceback.format_exc())
        return self.data_list



