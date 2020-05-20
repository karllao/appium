#test_case为测试用例文件夹
import unittest
import sys
from os.path import dirname,abspath
BASE_PATH = dirname(abspath(__file__))
sys.path.append(BASE_PATH)
from common.my_test import MyTest
from page.simple_page import SimplePage

class TestSimpleAdd(MyTest):

    def setUp(self):
        self.page = SimplePage(self.driver)
        self.page.clear_button.click()

    def test_int_add(self):
        '''测试整数相加'''

        self.page.num_2.click()
        self.page.plus_button.click()
        self.page.num_5.click()
        self.page.eq_button.click()
        result = MyTest.getclipboard(self,self.page.result_view)
        self.assertEqual('7',result)


    def test_decimal_add(self):
        '''测试小数相加'''

        self.page.num_2.click()
        self.page.dot_button.click()
        self.page.num_5.click()
        self.page.plus_button.click()
        self.page.num_5.click()
        self.page.dot_button.click()
        self.page.num_6.click()
        self.page.eq_button.click()
        result = MyTest.getclipboard(self,self.page.result_view)
        self.assertEqual('8.1',result)


    def test_percent_add(self):
        '''测试百分数相加'''

        self.page.num_5.click()
        self.page.per_button.click()
        self.page.plus_button.click()
        self.page.num_7.click()
        self.page.per_button.click()
        self.page.eq_button.click()
        result = MyTest.getclipboard(self,self.page.result_view)
        self.assertEqual('0.12',result)

if __name__ == '__main__':
    unittest.main()