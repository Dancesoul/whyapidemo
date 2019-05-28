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
secert="6410bdaa67df4f908cd98eae2948e712"   #appid
paradict={    #接口参数
"showapi_appid":"96053",
"keyword":"守株待兔"
}

showapi_sign=md5jiami(paradict,secert)   #调用上面写好的加密方法，加密appkey密码
paradict["showapi_sign"]=showapi_sign   #添加接口参数 showapi_sign

r=requests.post(url=url,data=paradict)  #url参数传入请求链接，data传入请求的参数

try:
	assert r.status_code==200,f"状态码不对 状态码是{r.status_code}"
	print(f"状态码正确 {r.status_code}")
except AssertionError as e:
	print(e)
