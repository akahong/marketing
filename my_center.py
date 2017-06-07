#encoding:utf-8
import unittest
from appium import webdriver
from time import sleep
from ddt import ddt,data,unpack


@ddt
class Imarketing_My_Center(unittest.TestCase):
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
    @data(('111111',' ',' '),('111111','111111',' '),('111111','111','111'),('111111','123456','1234567'))
    @unpack
    def test_changepwd(self,oldpwd,newpwd,confirmPwd):
        
        self.wd.find_element_by_id('id').send_keys('hdy123') #输入账号
        self.wd.find_element_by_id('pwd').send_keys('111111')#输入密码
        self.wd.find_element_by_id('YNTextView').click() #点击‘登陆’
        sleep(3)#等待3秒钟
        self.wd.find_element_by_id('own').click()#点击‘个人中心’
        sleep(2)#等待2秒钟
        self.wd.find_element_by_id('changePwd').click()#点击‘修改密码’
        for i in range(5):
            #print 'in for'
            self.wd.find_element_by_id('oldPwd').send_keys(oldpwd)#输入就密码
            
            self.wd.find_element_by_id('newPwd').send_keys(newpwd)#输入新密码
            
            self.wd.find_element_by_id('confirmPwd').send_keys(confirmPwd)#输入确认密码
            
            self.wd.find_element_by_id('finish').click()#点击完成
            sleep(4)#等待2秒钟
            
            elements=self.wd.find_elements_by_class_name('android.widget.EditText')# 获取密码输入框
            print 'android.widget.EditText'
            sleep(3)
            
            #for p in range(3):
                #print 'EditText_num:'+len(elements)
                #elements[p].clear()
            
            
        
        
    def tearDown(self):
        self.wd.quit()
        
        
if __name__=='__main__':
    unittest.main()
        