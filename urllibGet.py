import urllib.request
import urllib.parse
import json

url = 'http://127.0.0.1:9999/api/luckdraw/app/myLuckRecord?token=92175173d26241f28044126a942656cb&userId=15371&sign=1234'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'));
