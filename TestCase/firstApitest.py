#coding=utf-8
#Author miracle.why@qq.com 
import requests
import unittest
import json
import HTMLTestRunner
from common import conf,sqlhelper
import logging
import time
class whytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.host = conf.api_hosts['testhost']
        cls.whysql=sqlhelper.whysql()

    @classmethod
    def tearDownClass(cls):
        cls.whysql.close()
    def setUp(self):
        logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



    def test_checkdist_qtyofparameter(self):
        jiamicode ='bQDZ9a3Ze'
        url = "/v3/parts/%s/snapshots" % (jiamicode)
        r = requests.get(self.host + url)
        r=r.json()
        self.assertIn('dist_qtys',r)

    def test_httpcode(self):
        jiamicode = 'bQDZ9a3Ze'
        url = "/v3/parts/%s/snapshots" % (jiamicode)
        r = requests.get(self.host + url)
        self.assertEqual(r.status_code,200)



    def tearDown(self):
        msg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        msg+="运行Api测试"
        logging.info(msg)


