#encoding:utf-8
import unittest
from appium import webdriver
from time import sleep
from ddt import ddt,data,unpack


@ddt
class Imarketing_Home_Page(unittest.TestCase):
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
        
    def test_mask(self):
        self.wd.find_element_by_id('id').send_keys('hdy123') #输入账号
        self.wd.find_element_by_id('pwd').send_keys('111111')#输入密码
        self.wd.find_element_by_id('YNTextView').click() #点击‘登陆’
        sleep(3)#等待3秒钟     
        
        elemens=self.wd.find_elements_by_id('image')
        elemens[0].click()
        sleep(3)#等待3秒钟 
        
    def tearDown(self):
        self.wd.quit()
        
if __name__=='__main__':
    unittest.main()