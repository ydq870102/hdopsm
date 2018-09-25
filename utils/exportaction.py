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
        self.style = xlwt.XFStyle()
        self.style1 = xlwt.XFStyle()
        self.style2 = xlwt.XFStyle()
        self.template_file =os.path.join(os.getcwd() + '/static/excel', tempalte_file)
        self.query_set = query_set
        self.temp_file_name = tempalte_file.split('.')[0] + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.xls'
        self.export_file = os.path.join(os.getcwd() + '/temp', self.temp_file_name)
        if os.path.isdir(os.getcwd() + '/temp/') is not True:
            os.makedirs(os.getcwd() + '/temp/')
        self.related_column =[]

    def parse_data(self):
        self.execl_style()
        bk = xlrd.open_workbook(self.template_file)

        try:
            writebook = xlwt.Workbook(encoding='utf-8')
            write_sheet = writebook.add_sheet('template')
            read_sheet = bk.sheet_by_name("template")
            # 写入头文件
            for nr in range(0, 3):
                for lc in range(0, read_sheet.ncols):
                    if read_sheet.cell_value(nr, lc) == u'关联':
                        self.related_column.append(read_sheet.cell_value(1, lc))
                    sheet_value = read_sheet.cell_value(nr, lc)
                    write_sheet.write(nr, lc, sheet_value, self.style)
            # 写入内容
            for nr in range(0, len(self.query_set)):
                for lc in range(0, read_sheet.ncols):
                    if read_sheet.cell_value(1, lc) in self.related_column:
                        sheet_value = self.query_set[nr][read_sheet.cell_value(1, lc)+'_id']
                    else:
                        sheet_value = self.query_set[nr][read_sheet.cell_value(1, lc)]
                    if isinstance(sheet_value, (datetime.datetime)):
                        write_sheet.write(nr + 3, lc, sheet_value, self.style2)
                    else:
                        write_sheet.write(nr + 3, lc, sheet_value, self.style1)

            for lc in range(0, read_sheet.ncols):
                write_sheet.col(lc).width = 5000
            writebook.save(self.export_file)
            return self.export_file, self.temp_file_name
        except Exception, e:
            logger.error(traceback.format_exc())

    def execl_style(self):
        borders = xlwt.Borders()  # Create Borders
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 5
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
        font = xlwt.Font()
        font.bold = True
        font.name = 'Times New Roman'
        self.style.borders = borders
        self.style.pattern = pattern
        self.style.alignment = alignment
        self.style.font = font
        self.style1.borders = borders
        self.style1.alignment = alignment
        self.style2.borders = borders
        self.style2.alignment = alignment
        self.style2.num_format_str = 'yyyy/mm/dd'

