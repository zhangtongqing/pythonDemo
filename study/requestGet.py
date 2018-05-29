import requests
import json

url = 'http://127.0.0.1:9999/api/luckdraw/app/myLuckRecord?token=92175173d26241f28044126a942656cb&userId=15371&sign=1234'
ret = requests.get(url)

print(ret.text)