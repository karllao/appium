from poium import Page,PageElement,PageElements
from appium import webdriver
from common.my_test import MyTest

class SimplePage(Page):
    def __init__(self,driver):
        self.driver = driver
    #选择标准模式按钮
    simple_model = PageElement(class_name='flyme.support.v7.app.ActionBar$f')
    #数字键盘
    num_1 = PageElement(id_='com.meizu.flyme.calculator:id/digit1')
    num_2 = PageElement(id_='com.meizu.flyme.calculator:id/digit2')
    num_3 = PageElement(id_='com.meizu.flyme.calculator:id/digit3')
    num_4 = PageElement(id_='com.meizu.flyme.calculator:id/digit4')
    num_5 = PageElement(id_='com.meizu.flyme.calculator:id/digit5')
    num_6 = PageElement(id_='com.meizu.flyme.calculator:id/digit6')
    num_7 = PageElement(id_='com.meizu.flyme.calculator:id/digit7')
    num_8 = PageElement(id_='com.meizu.flyme.calculator:id/digit8')
    num_9 = PageElement(id_='com.meizu.flyme.calculator:id/digit9')
    num_0 = PageElement(id_='com.meizu.flyme.calculator:id/digit0')
    dot_button = PageElement(id_='com.meizu.flyme.calculator:id/dot')
    #运算符
    plus_button = PageElement(id_='com.meizu.flyme.calculator:id/plus')
    minus_button = PageElement(id_='com.meizu.flyme.calculator:id/minus')
    mul_button = PageElement(id_='com.meizu.flyme.calculator:id/mul')
    div_button = PageElement(id_='com.meizu.flyme.calculator:id/div')
    eq_button = PageElement(id_='com.meizu.flyme.calculator:id/eq')
    per_button = PageElement(id_='com.meizu.flyme.calculator:id/per')
    #编辑符
    clear_button = PageElement(id_='com.meizu.flyme.calculator:id/clear_simple')
    del_button = PageElement(id_='com.meizu.flyme.calculator:id/del_simple')

    #输出结果框
    result_view = PageElements(id_='com.meizu.flyme.calculator:id/edit_text')

    #result_view = self.driver.find_elements_by_id("com.meizu.flyme.calculator:id/edit_text")[-1]
