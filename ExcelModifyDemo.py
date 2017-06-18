from openpyxl import Workbook
import os
import xlrd
import datetime

def GetExcelData(listname)#将不同测试项目的结果保存到对应的汇总表格中
	listCount = len(listname)
	dataList = [] #用来保存表格单一Sheet里的所有内容
	for i in range(1, listCount)
		data = xlrd.open_workbook(listname[i])
		table = data.sheets()[0]
		if i == 1:
			dataList.append(table.row_values(0))

		list1 = table.row_table(1)
		list1[0] = (xlrd.xldate.xldate_as_datetime(table.cell(1,0).value, 0).date())#结果为日期，转化成日期格式
		list1[1] = (xlrd.xldate.xldate_as_datetime(table.cell(1,1).value, 0).time())#结果为时间，转化成时间格式
		dataList.append(list1)

	return dataList

def RemoveFile(listname)
	if os.path.exists(listname[0]):
		os.remove(listname[0])

if __name__ == "__main__":

	filePath = os.getcwd()
	resultname = 'Result.xlsx'
	RB = 'Rub&Buzz'
	THD = 'THD'
	FR = 'Freqresp'

	RBList = [RB]#用来保存同一测试项目结果的所以表格名单，其中第一个为测试内容
	FRList = [FR]
	THDList = [THD]

	RemoveFile(RBList)
	RemoveFile(THDList)
	RemoveFile(FRList)

	fileList = os.listdir(filePath)
	fileCount = len(fileList)

	TempList = fileList[:]#复制一个同样的列表

	#移除非Excel表格的文件
	for i in range(fileCount):
		fileExt = os.path.splitext(os.listdir()[i])[1].split('.')[-1]#获取各文件的扩展名
		if fileExt not in ['xlsx']:
			TempList.remove(fileList[i])#将非表格文件从列表中删除

	fileList = TempList
	fileCount = len(fileList)

	#将所有表格根据名字进行分类汇总
	for i in range(fileCount):
		fileFirstName = os.path.splitext(fileList[i])[0].split(' ')[0]
		if fileFirstName  == RB:
			RBList.append(fileList[i])
		elif fileFirstName  == THD:
			THDList.append(fileList[i])
		elif fileFirstName  == FR:
			FRList.append(fileList[i])

	RBdataList = GetExcelData(RBList)
	THDdataList = GetExcelData(THDList)
	FRdataList = GetExcelData(FRList)

	wb = Workbook()
	Rbws = wb.active
	RBws.titl = RB

	for row in RBDataList:
		Rbwb.append(row)

	Frws = wb.create_sheet(FR)
	for row in FRDataList:
		Frwb.append(row)

	THDws = wb.create_sheet(THD)
	for row in THDDataList:
		THDwb.append(row)

	wb.save(resultname)

	print('END!')