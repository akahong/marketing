#encoding:utf-8
import unittest
from appium import webdriver
from time import sleep
#import requests
import common
from ddt import ddt,data,unpack


@ddt
class Change_Pwd(unittest.TestCase):
    """个人中心"""
    
    def setUp(self):
        self.wd=common.star_up_appium()#调用启动appium方法 
    #----------------------------------------------------------------------
        
    def account_pwd_login(self):
        """输入账号密码登陆"""
        
        self.wd.find_element_by_id('id').send_keys('hdy123')#输入账号
        self.wd.find_element_by_id('pwd').send_keys('222222')#输入密码
        self.wd.find_element_by_id('YNTextView').click()  #点击‘登陆’按钮    
        sleep(3)
        #print self.wd.current_activity  #获取当前activity名  
        
    #----------------------------------------------------------------------
    def to_change_pwd_page(self):
        """跳转至修改密码页面"""
        
        self.wd.find_element_by_id('own').click()#点击‘个人中心’
        self.wd.find_element_by_id('textView3').click()#点击‘修改密码’
        
    #----------------------------------------------------------------------
    def input_pwd(self,oldpwd,newpwd,confirmpwd):
        """编辑密码输入框"""
        
        self.wd.find_element_by_id('oldPwd').send_keys(oldpwd)#输入旧密码
        self.wd.find_element_by_id('newPwd').send_keys(newpwd)#输入新密码
        self.wd.find_element_by_id('confirmPwd').send_keys(confirmpwd)#输入确认密码
        self.wd.find_element_by_id('finish').click()#点击‘完成’
        sleep(2)
        #self.wd.press_keycode(67) #删除键
        #self.wd.press_keycode(123)#将光标移到最后
        #self.wd.get_screenshot_as_file('pwd_least_6.png')#截屏         
        
    #----------------------------------------------------------------------    
    @data(('111111',' ',' '),('111111','111111',' '),('111111','111','111'),('111111','123456','1234567'))
    @unpack
    def test_changepwd(self,oldpwd,newpwd,confirmpwd):
        """修改密码case入口"""
        
        #判断当前页面是否为首页
        if self.wd.current_activity=='.activity.MainActivity':
            
            #调用跳转至修改密码页面方法
            self.to_change_pwd_page() 
            
            #调用编辑密码输入框方法
            self.input_pwd(oldpwd, newpwd, confirmpwd)
                
        else:
            
            #调用登陆方法
            self.account_pwd_login()
        
            #调用跳转至修改密码页面方法
            self.to_change_pwd_page()
            
            #调用编辑密码输入框方法
            self.input_pwd(oldpwd, newpwd, confirmpwd)
            
    #----------------------------------------------------------------------
    def test_brand_collection(self):
        """品牌收藏case入口"""
        
        self.wd.find_element_by_id('own').click()#点击‘个人中心’
        
        #点击‘品牌收藏’
        self.wd.find_elements_by_class_name('android.widget.TextView')[2].click()
        #print self.wd.current_activity
    
    #----------------------------------------------------------------------          
        def tearDown(self):
            self.wd.quit()    
########################################################################
class Change_Language(unittest.TestCase):
    """语言切换"""

    #----------------------------------------------------------------------
    def setUp(self):
        self.wd=common.star_up_appium()#调用启动appium方法 
        
        #点击‘个人中心’ 
        self.wd.find_element_by_id('own').click()    
        
        #点击'语言切换’
        self.wd.find_elements_by_class_name('android.widget.TextView')[3].click()     
        
    #----------------------------------------------------------------------
    def test_left_button(self):
        """判断‘<’功能"""
        
        self.wd.find_element_by_id('leftImageView').click()#
        if self.wd.current_activity=='.activity.MainActivity':
            print '返回个人中心'
        else:
            print '页面跳转失败'
            
    #----------------------------------------------------------------------
    def test_switch_chinese(self):
        """切换系统语言为中文"""
        self.wd.find_elements_by_class_name('android.widget.TextView')[1].click()#
        self.wd.find_element_by_id('leftButton').click()#
        chinese=self.wd.find_element_by_id('title').text
        
        if self.assertEqual(u'首页', chinese):
            print '系统语言为中文'
        else:
            print '系统语言切换失败'
            
    #----------------------------------------------------------------------          
    def tearDown(self):
        self.wd.quit()
        
        
if __name__=='__main__':
    case=unittest.TestSuite()
    case.addTest(Change_Language('test_switch_chinese'))
    
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(case)
    
        