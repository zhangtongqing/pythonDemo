#coding:utf-8
import itchat
import shutil
import math
import PIL.Image as Image
import os
import itchat as itchat

itchat.auto_login(hotReload = True)

#获取好友信息
friends = itchat.get_friends(update=True)[0:] #（当然你也可以进行输出，但是小编是看的头晕）
user = friends[0]["UserName"]
print("user:",user)
if os.path.exists(user):
    shutil.rmtree(user) #递归删除所有文件
os.mkdir(user)

#获取好友头像并保存在目录文件夹下
num = 0
for friend in friends:
    image = itchat.get_head_img(userName=friend["UserName"]) #用 itchat.get_head_img(userName=None)来爬取好友列表的头像
    fileImage = open(user + "/" + str(num) + ".jpg",'wb') #将好友头像下载到本地文件夹
    fileImage.write(image)
    fileImage.close()
    num += 1

#将微信图像进行拼接
dirs = os.listdir("/")
each_size = int(math.sqrt(float(640*640)/len(dirs)))
line = int(640.0/each_size)
photographic = Image.new("RGB",(640,640))
x = 0
y = 0
for i in range(0,len(dirs)):
    try:
        imageOfFriends = Image.open(user + "/" + str(i) + ".jpg") #打开头像拼接照片，PIL库的应用
    except IOError:
        print("error")
    else:
        image_resize = imageOfFriends.resize((each_size,each_size))
        photographic.paste(image_resize,(x*each_size,y*each_size))
        x += 1
        if x == line:
            x = 0
            y += 1



#保存图像，发送给文件助手，显示图像
photographic.save(user + "/" + "all.jpg") #保存拼接图片至当前目录
itchat.send_image(user + "/" + "all.jpg","filehelper") #把图片发送给微信文件助手（filehelper
photographic.show()
print("展示拼接成的头像图片")

"""
 运行扫码登录后，程序会执行：
 1.拉取好友们的头像，写在当前目录；
 2.延迟弹窗拼接头像图片
 3.通过文件助手，发送头像拼接图片
"""