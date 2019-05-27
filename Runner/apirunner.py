#coding=utf-8
#Author miracle.why@qq.com 
import HTMLTestRunner
from TestCase import firstApitest
import unittest
import time

from TestCase import Proverbsearch
from TestData import fileData


def filerunner():
    p=Proverbsearch.proverb()
    return p.test_httpcode_200_frompythonfile(fileData.test_http_code_200)

def Unittestrunner():
    Now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    f = open("D:\ApiTestDemo\Report\\" + Now + ".html", "wb")
    t = firstApitest.whytest()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(firstApitest.whytest)
    APIRuner = HTMLTestRunner.HTMLTestRunner(f, title=Now.replace('_', ':') + " ApiTestReport", description='这个是备注')
    APIRuner.run(suite)
    f.close()

def DataBaserunner():
    p=Proverbsearch.proverb()
    return p.test_httpcode_200_fromDataBase()


if __name__=="__main__":
    #print(filerunner())
    print(DataBaserunner())
