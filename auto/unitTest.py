import unittest

class TestMathFunc(unittest.TestCase):

    def test_add(self):
        print("单元测试第一个方法")

    def test_add1(self):
        print("单元测试第二个方法")

if __name__ == '__main__':
    unittest.main()

"""
 单元测试类用法：运行main 则，单元测试类里所有方法
 单个测试方法运行： 选中方法名，右键运行
"""