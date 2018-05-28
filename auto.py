from api import SignUtil
import requests
from urllib import parse
import unittest


class MyTestSuite(unittest.TestCase):
    #自动化测试实例
    def sedUp(self):
        print("start...");

    def test_01(self):
        import json
        # 请求URL
        url = "http://211.159.153.228:8080/api//luckdraw/app/myLuckRecord";
        # 公共参数
        parames = {
            "token": "92175173d26241f28044126a942656cb",  # 用户token
            "userId": 15371  # 用户ID
        }

        # 获取签名
        sign = SignUtil.getSign(url, parames, "");
        # 拼装请求URL
        url += "?" + parse.urlencode(parames) + "&sign=" + sign

        # **********************************************************************
        headers = {'content-type': 'application/json'}
        ret = requests.get(url, parames)
        data = json.loads(ret.text)  # 转换成json对象
        json = json.dumps(data, ensure_ascii=False, indent=2);  # 格式化json ensure_ascii=False 不编译中文，indent=2 换行
        print(json)


    def test_02(self):
        import json
        url = "http://211.159.153.228:8080/api//running/pc/getRunningRecordAppealInfo";
        # 公共参数
        parames = {
            "token": "9701ccf45c6c480397aa8d461340261e",  # 用户token
            "userId": 15200,  # 用户ID
        }

        # 参数
        body = {
            "runningRecordId": "127520820180518141815792"
        };
        sign = SignUtil.getSign(url, parames, body);
        # 拼装请求URL
        url += "?" + parse.urlencode(parames) + "&sign=" + sign
        headers = {'content-type': 'application/json'}
        ret = requests.post(url, data=json.dumps(body), headers=headers)
        data = json.loads(ret.text)  # 转换成json对象
        json = json.dumps(data, ensure_ascii=False, indent=2);  # 格式化json ensure_ascii=False 不编译中文，indent=2 换行
        print(json)

#构造测试集合
suite = unittest.TestSuite();
suite.addTest(MyTestSuite("test_01"));
suite.addTest(MyTestSuite("test_02"));


#执行测试
runner = unittest.TextTestRunner();
runner.run(suite);