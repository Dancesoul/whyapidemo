#coding=utf-8
#Author miracle.why@qq.com
import pymysql

class whysql():
    def __init__(self):
        self.connect=pymysql.connect(
            host='',    #数据库ip
            port=3306,   #数据口端口号
            user='',     #数据库用户名
            password='',    #密码
            db='',          #数据库名
            charset='utf8'    #数据库字符集
        )

    def gettestdata(self,test_casename=None):
        '''
        :param test_casename: 测试用例名字  默认没有，取全部数据
        :return: 返回测试用例数据 成功返回dict 失败返回-1
        '''
        cursor=self.connect.cursor(cursor=pymysql.cursors.DictCursor)

        if test_casename is None:
            sql = 'SELECT * from test_info'
        else:
            sql = 'SELECT * from test_info where test_case_name = "%s"' % (test_casename)

        if (int(cursor.execute(sql))>0):
            per=cursor.fetchall()    #把查询结果集放到per中
        else:
            per=-1
        cursor.close()   #关闭游标
        self.connect.commit()    #提交数据库事务
        return per
    def close(self):
        self.connect.close()