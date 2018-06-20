#coding=utf-8
###################### 完整代码##############################
# 加载库
from itchat.content import *
import requests
import json
import itchat

"""
将根据接受到的消息类型寻找对应的已注册的方法.
如果一个消息类型没有对应的注册方法, 该消息将会被舍弃.
在运行过程中也可以动态注册方法, 注册方式与结果不变.
"""
itchat.auto_login(hotReload = True)


# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
  appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
  url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
  req = requests.get(url)
  content = req.text
  data = json.loads(content)
  answer = data['text']
  return answer


# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
def group_id(name):
  df = itchat.search_chatrooms(name=name)
  return df[0]['UserName']


# 注册文本消息，绑定到text_reply处理函数
# text_reply msg_files可以处理好友之间的聊天回复
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
  itchat.send('%s' % tuling(msg['Text']),msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
  msg['Text'](msg['FileName'])
  return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])



# 现在微信加了好多群，并不想对所有的群都进行设置微信机器人，只针对想要设置的群进行微信机器人，可进行如下设置
@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
  # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
  item = group_id(u'Python学习交流群') # 根据自己的需求设置
  if msg['FromUserName'] == item:
    itchat.send(u'%s' % tuling(msg['Text']), item)

@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
  item = group_id(u'四大名捕') # 根据自己的需求设置
  if msg['FromUserName'] == item:
    itchat.send(u'%s' % tuling(msg['Text']), item)


friends = itchat.get_friends(update=True)
itchat.run()