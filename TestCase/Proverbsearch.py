#coding=utf-8
#Author miracle.why@qq.com
import hashlib

import requests
from TestData import fileData

from common import sqlhelper

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

