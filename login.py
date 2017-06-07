#encoding:utf-8
import unittest
from appium import webdriver
from time import sleep
from ddt import ddt,data,unpack
import common

@ddt
class Imarketing_Longin(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVesion']='6.0'
        desired_caps['deviceName']='HUAWEI MT7-TL00'
        desired_caps['appPackage']='com.bcc.bestselling'
        desired_caps['appActivity']='com.bcc.bestselling.activity.LogoActivity'
        desired_caps['unicodeKeyboard']='True'
        desired_caps['resetKeyboard']='True'

        self.wd=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(3)
        
    @data(('hdy123','1233'),('hdy123','12333333'),(' ','123777777'),('hdy123','111111')) 
    @unpack
    def test_login(self,account,password):
        
        self.wd.find_element_by_id('id').send_keys(account)
        self.wd.find_element_by_id('pwd').send_keys(password)
        self.wd.find_element_by_id('YNTextView').click()
        sleep(3)
        
    def test_checkbox(self):
        self.wd.find_element_by_id('checkbox').click()
        sleep(2)
        self.wd.find_element_by_id('checkbox').click()
        sleep(2)
        
    def test_clause(self):
        self.wd.find_element_by_id('privacyPolicy').click()
        sleep(2)
        self.wd.find_element_by_id('left').click()
        sleep(2)
        
    def tearDown(self):
        self.wd.quit()
        
if __name__=='__main__':
    unittest.main()
        