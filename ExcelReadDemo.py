import xlrd
import os

if __name__ == "__main__":
    filename = "Demo2.xls"
    os.chdir(os.getcwd())
    excelRd = xlrd.open_workbook(filename) #打开要读取的表格

    print(excelRd.sheet_names()) #获取表格中所有页的名称

    sheet = excelRd.sheets()[0] #获取表格中的页1
    #sheet = excelRd.sheet_by_index(0) #获取表格中的页1
    #sheet = excelRd.sheet_by_name(u'Sheet1') #通过名称来获取表格中对应的页

    nrows = sheet.nrows #获取当前页中有多少行数据
    ncols = sheet.ncols #获取当前页中有多少列数据
    print(nrows) 
    print(ncols)
    for i in range(nrows ):
      print(sheet.row_values(i)) #分别打印出当前页下每一行的数据

    cell_A1 = sheet.cell(0,0).value #获取对应行列的表格的内容   需要注意的是读取的表格内容不能超过范围
    cell_C4 = sheet.cell(rowx=3,colx=2).value #获取对应行列的表格的内容
    print(cell_A1)
    print(cell_C4)

