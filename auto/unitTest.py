import unittest

import requests

class TestMathFunc(unittest.TestCase):

    def test_add1(self):
        print("单元测试第一个方法")

    def test_add(self):
        import json
        # 请求URL
        url = "http://211.159.153.228:8080/api/version/app/getMaxVersionByClient?t=ANDROID&v=2.0.1";

        # **********************************************************************
        ret = requests.get(url)
        data = json.loads(ret.text)  # 转换成json对象
        json = json.dumps(data, ensure_ascii=False, indent=2);  # 格式化json ensure_ascii=False 不编译中文，indent=2 换行
        print(json)




if __name__ == '__main__':
    unittest.main()

"""
 单元测试类用法：运行main 则，单元测试类里所有方法
 单个测试方法运行： 选中方法名，右键运行
"""