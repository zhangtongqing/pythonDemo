import json
import requests

#请求URL
url = "http://211.159.153.228:8080/api/version/app/getMaxVersionByClient?t=ANDROID&v=2.0.1";

#**********************************************************************
headers = {'content-type': 'application/json'}
ret = requests.get(url)
data = json.loads(ret.text) #转换成json对象
json = json.dumps(data,ensure_ascii=False,indent=2);#格式化json ensure_ascii=False 不编译中文，indent=2 换行
print(json)





