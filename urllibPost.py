import urllib.request
import urllib.parse
import json


url='http://127.0.0.1:9999/api/running/pc/getStudentAppealList?token=9701ccf45c6c480397aa8d461340261e&userId=15200&sign=5153714e731ff518cf272335fd1a4900&t=pc'
data={
	"pageindex": 1,
	"pagesize": 20,
	"status": "-1",
	"courseArray": "",
	"queryType": 1,
	"queryString": ""
};
data = json.dumps(data);
data=bytes(data,'utf8');
request=urllib.request.Request(url);
#设置header 常见的四种编码方式如下：1）application/x-www-form-urlencoded 2）multipart/form-data   3）application/json   4）text/xml
request.add_header("Content-Type", "application/json");
result=urllib.request.urlopen(request,data).read();
print(result);
