from api import SignUtil
import requests
import json
from urllib import parse

#请求URL
url = "http://211.159.153.228:8080/api//luckdraw/app/myLuckRecord";
#公共参数
parames ={
    "token":"92175173d26241f28044126a942656cb", #用户token
    "userId":15371  #用户ID
}


#获取签名
sign = SignUtil.getSign(url, parames, "");
#拼装请求URL
url +=  "?"+parse.urlencode(parames)+"&sign="+sign

#**********************************************************************
headers = {'content-type': 'application/json'}
ret = requests.get(url,parames)
data = json.loads(ret.text) #转换成json对象
json = json.dumps(data,ensure_ascii=False,indent=2);#格式化json ensure_ascii=False 不编译中文，indent=2 换行
print(json)





