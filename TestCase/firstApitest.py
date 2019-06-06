#coding=utf-8
#Author miracle.why@qq.com 
import requests
import unittest
import json
import HTMLTestRunner
from common import conf,sqlhelper,common
import time

class whytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   #框架开始运行时的初始化方法
        pass

    @classmethod
    def tearDownClass(cls):   #框架运行结束时的方法
        pass

    def setUp(self):   #每个测试用例开始前的初始化方法
        pass

    def tearDown(self):   #每个用例结束后的方法
        pass

    def test_httpcode_200_fromexcel(self):   #测试用例
        excelinfo = common.getexcleinfo("test_httpcode_200_fromexcel")
        testinfo = eval(excelinfo[1])  # 返回的内容是list 我们取第二个位置就是输入数据

        url = testinfo["url"]  # 接口url
        secert = testinfo["secert"]  # appid
        paradict = testinfo["paradict"]  # 参数

        showapi_sign = common.md5jiami(paradict, secert)  # 调用上面写好的加密方法，加密appkey密码
        paradict["showapi_sign"] = showapi_sign  # 添加接口参数 showapi_sign

        r = requests.post(url=url, data=paradict)  # url参数传入请求链接，data传入请求的参数
        return self.assertEqual(r.status_code, testinfo["testinfo"], "测试未通过 状态码是 ")





