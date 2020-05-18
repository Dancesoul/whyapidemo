#coding=utf-8
#Author miracle.why@qq.com
import requests   #导入requests模块
import hashlib    #这个模块是用来加密的 md5，sha1 等
def md5jiami(paradict,secert):
	jiamistr = ""
	for key in sorted(paradict.keys()):
		jiamistr = jiamistr + str(key) + str(paradict[key])
	jiamistr = jiamistr + secert
	showapi_sign = (hashlib.md5(jiamistr.encode(encoding='UTF-8')).hexdigest())
	return showapi_sign

url="http://route.showapi.com/1196-2"   #接口url
secert="6410bdaa67df4f908cd98eae2948e712"   #appkey
paradict={    #放接口参数的字典
"showapi_appid":"96053",
"keyword":"守株待兔"
}

showapi_sign=md5jiami(paradict,secert)   #加密appkey密码
paradict["showapi_sign"]=showapi_sign    #添加接口参数 showapi_sign

#下面这部分构造get请求的url  构造格式大概是 请求url?参数1=参数值&参数2=参数值

geturl=url+"?"
for key in paradict.keys():
	geturl=geturl+"&"+key+"="+paradict[key]

getr=requests.get(geturl)  #调用http的get请求

print(getr.status_code)  #打印请求状态码
print(getr.text)      #打印返回内容  
print(getr.json())       #打印返回内容  json格式
