from selenium import webdriver


#selenium是一个用于Web应用程序测试的工具
#下载geckodriver.exe firefox的浏览器驱动，防止python安装目录，python.exe同级目录
browser = webdriver.Firefox()
browser.get('http://www.baidu.com')