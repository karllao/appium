#test_case为测试用例文件夹
import unittest
import sys
from os.path import dirname,abspath
BASE_PATH = dirname(abspath(__file__))
sys.path.append(BASE_PATH)
from common.my_test import MyTest
from page.simple_page import SimplePage

class TestSimpleSub(MyTest):

    def setUp(self):
        self.page = SimplePage(self.driver)
        self.page.clear_button.click()

    def test_int_sub(self):
        '''测试整数相减'''

        self.page.num_8.click()
        self.page.minus_button.click()
        self.page.num_5.click()
        self.page.eq_button.click()
        result = MyTest.getclipboard(self,self.page.result_view)
        self.assertEqual('3',result)


    def test_decimal_sub(self):
        '''测试小数相减'''

        self.page.num_6.click()
        self.page.dot_button.click()
        self.page.num_5.click()
        self.page.minus_button.click()
        self.page.num_2.click()
        self.page.dot_button.click()
        self.page.num_6.click()
        self.page.eq_button.click()
        result = MyTest.getclipboard(self,self.page.result_view)
        self.assertEqual('3.8',result)


    def test_percent_sub(self):
        '''测试百分数相减'''

        self.page.num_7.click()
        self.page.per_button.click()
        self.page.minus_button.click()
        self.page.num_5.click()
        self.page.per_button.click()
        self.page.eq_button.click()
        result = MyTest.getclipboard(self,self.page.result_view)
        self.assertEqual('0.02',result)

if __name__ == '__main__':
    unittest.main()