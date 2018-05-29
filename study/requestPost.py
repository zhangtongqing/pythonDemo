import requests
import json

url = 'http://127.0.0.1:9999/api/running/pc/getStudentAppealList?token=9701ccf45c6c480397aa8d461340261e&userId=15200&sign=5153714e731ff518cf272335fd1a4900&t=pc'
payload = {
	"pageindex": 1,
	"pagesize": 20,
	"status": "-1",
	"courseArray": "",
	"queryType": 1,
	"queryString": ""
}
headers = {'content-type': 'application/json'}
ret = requests.post(url, data=json.dumps(payload), headers=headers)

print(ret.text)