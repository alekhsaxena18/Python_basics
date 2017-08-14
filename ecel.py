import xlrd
import xlwt
from xlutils.copy import copy
def saveWorkSpace(fields):
    rb = xlrd.open_workbook('C:\\Users\\Alekh\\Desktop\\accounts.xls',formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(r,0,fields['name'])
    sheet.write(r,1,fields['phone'])
    sheet.write(r,2,fields['email'])
    wb.save('C:\\Users\\Alekh\\Desktop\\accounts.xls')
