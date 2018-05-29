from api import SignUtil
import requests
import json
from urllib import parse

#请求URL
url = "http://211.159.153.228:8080/api/schoolUser/pc/getStudentList";
#公共参数
parames ={
    "token":"9701ccf45c6c480397aa8d461340261e", #用户token
    "userId":15200, #用户ID
    "sign":"xxx"
}

#参数
body = {
	"status": 0,
	"pageindex": "1",
	"pagesize": 20
}

#**********************************************************************
#拼装请求URL
url +=  "?"+parse.urlencode(parames)
headers = {'content-type': 'application/json'}
ret = requests.post(url,data=json.dumps(body), headers=headers)
data = json.loads(ret.text) #转换成json对象
json = json.dumps(data,ensure_ascii=False,indent=2);#格式化json ensure_ascii=False 不编译中文，indent=2 换行
print(json)