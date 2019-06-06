#coding=utf-8
#Author miracle.why@qq.com
import hashlib

import xlrd


def md5jiami(paradict, secert):
	jiamistr = ""
	for key in sorted(paradict.keys()):
		jiamistr = jiamistr + str(key) + str(paradict[key])
	jiamistr = jiamistr + secert
	showapi_sign = (hashlib.md5(jiamistr.encode(encoding='UTF-8')).hexdigest())
	return showapi_sign


def getexcleinfo(casename):
	'''
	path 是excel地址
	:param casename:测试用例名字
	:return:  返回测试用例的字典
	'''
	path = "../TestData/testcases.xlsx"
	rdbook = xlrd.open_workbook(path, encoding_override="utf-8")  # 新建一个xlrd对象，path是excel路径，encoding_override是编码
	rdsheet = rdbook.sheet_by_index(0)  # 按索引取第一个sheet
	casenames = rdsheet.col_values(0)  # 因为我们第一列是测试用例名字  所以取出所有的测试用例名字
	caseindex = casenames.index(casename)  # 找到我们要找的测试用例名字 在所有测试用例中是第几行
	res = rdsheet.row_values(caseindex)  # 通过上一步找到的行的位置 来获取这一行的所有信息，也就是我们测试用例的信息
	return res