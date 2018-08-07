#!/usr/bin/env python
# encoding: utf-8

import os
import xlrd, xlwt
import datetime
import logging
import traceback
logger = logging.getLogger('django')


class ExportAction(object):
    def __init__(self, query_set, tempalte_file):

        self.template_file = 'static/excel/' + tempalte_file
        self.query_set = query_set
        self.temp_file_name = tempalte_file.split('.')[0]+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.xls'
        self.export_file = os.path.join(os.getcwd() + '/temp/', self.temp_file_name)


    def parse_data(self):
        bk = xlrd.open_workbook(self.template_file)
        try:
            writebook = xlwt.Workbook(encoding = 'utf-8')
            write_sheet = writebook.add_sheet('template')
            read_sheet = bk.sheet_by_name("template")
            # 写入头文件
            for nr in range(0,3):
                for lc in range(0, read_sheet.ncols):
                    write_sheet.write(nr, lc, read_sheet.cell_value(nr, lc))
            # 写入内容
            for nr in range(0, len(self.query_set)):
                for lc in range(0, read_sheet.ncols):
                    write_sheet.write(nr+3, lc, self.query_set[nr][read_sheet.cell_value(1, lc)])

            writebook.save(self.export_file)
            return self.export_file, self.temp_file_name
        except Exception, e:
            logger.error(traceback.format_exc())



