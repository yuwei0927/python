import xlwt

if __name__ == "__main__":
    workbook = xlwt.Workbook() #创建workbook对象,注意Workbook的开头W要大写
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True) #创建表格sheet对象
    sheet2 = workbook.add_sheet('test1',cell_overwrite_ok=True) #创建表格sheet对象
    #向sheet页中的对应位置写入数据
    #sheet.write(row, col, contents, style)
    sheet1.write(0,0,'this should overwrite1')
    sheet1.write(0,1,'aaaaaaaaaaaa')
    sheet2.write(0,0,'this should overwrite2')
    sheet2.write(1,2,'bbbbbbbbbbbbb')

    style = xlwt.XFStyle() # Initialize a style
     
    # Create a font to use with the style
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = True
     
    # Set the style's font to this new one you set up
    style.font = font
     
    # Use the style when writing
    sheet1.write(2, 2, 'some bold Times text', style)
    #保存该excel文件,有同名文件时直接覆盖
    workbook.save('test2.xls')

