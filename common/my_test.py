#common文件夹为存放公共模块
import unittest
from appium import webdriver
import sys
from os.path import dirname,abspath
BASE_PATH = dirname(abspath(__file__))
sys.path.append(BASE_PATH)
from app_config import CAPS
from appium.webdriver.common.touch_action import TouchAction

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub',CAPS)
        cls.driver.implicitly_wait(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def getclipboard(cls,result_view):
        TouchAction(cls.driver).long_press(result_view[-1], duration=1500).perform()
        TouchAction(cls.driver).tap(x=546, y=846).perform()
        result = cls.driver.get_clipboard_text()
        return result