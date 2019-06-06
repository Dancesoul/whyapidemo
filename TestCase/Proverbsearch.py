#coding=utf-8
#Author miracle.why@qq.com
import hashlib

import requests
from TestData import fileData

from common import sqlhelper

import xlrd

class proverb():
	def __init__(self):
		self.whysql=sqlhelper.whysql()
	def assertEqual(self,A,B,msg):
		try:
			assert A == B
			return True
		except AssertionError:
			return msg+str(A)

	def md5jiami(self,paradict, secert):
		jiamistr = ""
		for key in sorted(paradict.keys()):
			jiamistr = jiamistr + str(key) + str(paradict[key])
		jiamistr = jiamistr + secert
		showapi_sign = (hashlib.md5(jiamistr.encode(encoding='UTF-8')).hexdigest())
		return showapi_sign

	def getexcleinfo(self,casename):
		'''
		path 是excel地址
		:param casename:测试用例名字
		:return:  返回测试用例的字典
		'''
		path="../TestData/testcases.xlsx"
		rdbook=xlrd.open_workbook(path,encoding_override="utf-8")   #新建一个xlrd对象，path是excel路径，encoding_override是编码
		rdsheet=rdbook.sheet_by_index(0)  #按索引取第一个sheet
		casenames=rdsheet.col_values(0)       #因为我们第一列是测试用例名字  所以取出所有的测试用例名字
		caseindex=casenames.index(casename)    #找到我们要找的测试用例名字 在所有测试用例中是第几行
		res=rdsheet.row_values(caseindex)        #通过上一步找到的行的位置 来获取这一行的所有信息，也就是我们测试用例的信息
		return res



	def test_httpcode_200_frompythonfile(self,testinfo):

		url = testinfo["url"]  # 接口url
		secert = testinfo["secert"]  # appid
		paradict = testinfo["paradict"]  #参数

		showapi_sign = self.md5jiami(paradict, secert)  # 调用上面写好的加密方法，加密appkey密码
		paradict["showapi_sign"] = showapi_sign  # 添加接口参数 showapi_sign

		r = requests.post(url=url, data=paradict)  # url参数传入请求链接，data传入请求的参数
		return self.assertEqual(r.status_code,testinfo["testinfo"],"测试未通过 状态码是 ")

	def test_httpcode_200_fromDataBase(self):

		whysql=self.whysql
		res=whysql.gettestdata("test_httpcode_200_fromDataBase")   #调用sqlhelper的方法来获取数据
		whysql.close()
		testinfo=eval(res[0]["case_infos"]) #注意返回的是list，然后具体的测试内容是字符串 所以需要取索引0的测试数据再转化成字典
		url = testinfo["url"]  # 接口url
		secert = testinfo["secert"]  # appid
		paradict = testinfo["paradict"]  # 参数

		showapi_sign = self.md5jiami(paradict, secert)  # 调用上面写好的加密方法，加密appkey密码
		paradict["showapi_sign"] = showapi_sign  # 添加接口参数 showapi_sign

		r = requests.post(url=url, data=paradict)  # url参数传入请求链接，data传入请求的参数
		return self.assertEqual(r.status_code, testinfo["testinfo"], "测试未通过 状态码是 ")

	def test_httpcode_200_fromexcel(self):
		excelinfo=self.getexcleinfo("test_httpcode_200_fromexcel")
		testinfo=eval(excelinfo[1])  #返回的内容是list 我们取第二个位置就是输入数据

		url = testinfo["url"]  # 接口url
		secert = testinfo["secert"]  # appid
		paradict = testinfo["paradict"]  # 参数

		showapi_sign = self.md5jiami(paradict, secert)  # 调用上面写好的加密方法，加密appkey密码
		paradict["showapi_sign"] = showapi_sign  # 添加接口参数 showapi_sign

		r = requests.post(url=url, data=paradict)  # url参数传入请求链接，data传入请求的参数
		return self.assertEqual(r.status_code, testinfo["testinfo"], "测试未通过 状态码是 ")



