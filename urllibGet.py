import urllib.request
import urllib.parse
import json

url = 'http://211.159.153.228:8080/api/luckdraw/app/myLuckRecord?token=92175173d26241f28044126a942656cb&userId=15371&sign=1234'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'));
