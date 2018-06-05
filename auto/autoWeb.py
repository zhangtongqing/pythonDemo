# coding = utf-8
from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://211.159.159.175:3006/")
#输入用户名密码
browser.find_element_by_id("nickname").send_keys("admin")
browser.find_element_by_id("password").send_keys("000000")
#点击登录
browser.find_element_by_class_name("login-form-button").click()
print("打开官方网站："+browser.current_url)

browser.get("http://211.159.159.175:3005/")
#输入用户名密码
browser.find_element_by_id("nickname").send_keys("qdladmin")
browser.find_element_by_id("password").send_keys("123456")
#点击登录
browser.find_element_by_class_name("login-form-button").click()
print("打开校方网站："+browser.current_url)