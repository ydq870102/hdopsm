#!/usr/bin/env python
# encoding: utf-8

import os
import xlrd


class ImportAction(object):
    def __init__(self, request):
        self.import_file = request.FILES.get('import_file')
        self.upload_file = ''

    def save_file(self):
        self.upload_file = os.path.join(os.getcwd() + '/upload/', self.import_file.name)
        if os.path.isdir(os.path.dirname(self.upload_file)) is not True: os.makedirs(os.path.dirname(self.upload_file))
        fobj = open(self.upload_file, 'wb')
        for chrunk in self.import_file.chunks():
            fobj.write(chrunk)
        fobj.close()

    def get_data(self):
        self.save_file()
        bk = xlrd.open_workbook(self.upload_file)
        dataList = []
        try:
            template = bk.sheet_by_name("template")
            max_row = self.get_excel_max_row(template)
            for i in range(2, template.nrows):
                dataList.append(template.row_values(i))
            print dataList
        except Exception, e:
            return []
        return dataList

    def get_excel_max_row(self,sheet):
        max_row = 0
        for row in sheet.row_values(1):
            if row:
                max_row = max_row + 1
        return max_row