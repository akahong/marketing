#encoding:utf-8

import unittest
from appium import webdriver
from time import sleep,strftime
#from ddt import ddt,data,unpack
import common
from PIL import Image
import pytesseract
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Imarketing_Longin(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVesion']='6.0'
        desired_caps['deviceName']='HUAWEI MT7-TL00'
        desired_caps['appPackage']='com.bcc.bestselling'
        desired_caps['appActivity']='com.bcc.bestselling.activity.LogoActivity'
        #desired_caps['unicodeKeyboard']='True'
        #desired_caps['resetKeyboard']='True'

        self.wd=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(3)
    
    def tearDown(self):
        self.wd.quit()    
        
class Login_Page_Display(Imarketing_Longin): 
    """登陆页面，页面文案显示"""
    
    #登陆页面的title是否为‘登陆’
    def test_title(self):
        """登陆页面的title是否为‘登录’"""
        title=self.wd.find_element_by_id('title').text
        self.assertEqual(title, u'登录')
        
    #登陆页面账号输入框隐体字
    def test_account_yintizi(self):
        """账号输入框的隐体字是否为‘请输入账号’"""
        id=self.wd.find_element_by_id('id').text
        self.assertEqual(id, u'请输入账号')
        
    #登陆页面密码输入框隐体字  
    @unittest.skip('直接跳过')
    def test_pwd_yintizi(self):
        """密码输入框的隐体字是否为‘请输入密码’"""
        pwd=self.wd.find_element_by_id('pwd').text
        try:
            self.assertEqual(pwd,u'请输入密码',msg=u'结果与预期不符')
        except Exception as e:
            print e        
        
    #‘保存密码，自动登陆’文案是否正确
    def test_checkbox_copywriter(self):
        """‘保存密码,自动登录’文案是否正确"""
        copywrite1=self.wd.find_element_by_id('textView2').text
        self.assertEqual(copywrite1,u'保存密码,自动登录')
        
    #登陆按钮文案
    def test_login_copywrite(self):
        """登录按钮的文案是否为‘登录’"""
        copywrite2=self.wd.find_element_by_id('YNTextView').text.strip()
        self.assertEqual(copywrite2,u'登录')
        
    #‘登陆即表示同意’文案是否正确
    def test_prive_copywrite(self):
        """‘登录即表示同意’文案是否正确"""
        copywrite3=self.wd.find_elements_by_class_name('android.widget.TextView')[3].text
        self.assertEqual(copywrite3,u'登录即表示同意')
        
    #
        
    #‘隐私条款’链接文案是否正确
    def test_prive_link(self):
        """‘隐私条款’链接文案是否正确"""
        link=self.wd.find_elements_by_class_name('android.widget.TextView')[4].text
        self.assertEqual(link,u'《隐私条款》')
        
class Login_Features(Imarketing_Longin):
    """登陆页面页面功能"""
        
    #光标聚焦账号输入框中，是否弹出全键盘
    def test_account_cursor(self):
        """光标聚焦账号输入框中，是否弹出全键盘"""
        #self.wd.press_keycode(4)
        self.wd.find_element_by_id('id').click()
        filename='account_cursor_keyboard.png'
        self.wd.get_screenshot_as_file(filename)
        img=Image.open(filename)
        results=pytesseract.image_to_string(img)
        print results
        self.assertIn('q',results)
        
    #光标聚焦密码输入框，是否弹出全键盘
    def test_pwd_cursor(self):
        """光标聚焦密码输入框，是否弹出全键盘"""
        self.wd.find_element_by_id('pwd').click()
        filename='pwd_cursor_keyboard.png'
        self.wd.get_screenshot_as_file(filename)
        img=Image.open(filename)
        results=pytesseract.image_to_string(img)
        print results
        self.assertIn('q',results) 
        
    #未编辑输入框，点击‘登陆’，弹出‘请输入账号’
    def test_none_login(self):
        """未编辑输入框，点击‘登陆’，是否提示‘请输入账号’"""
        filename='account_none.png'
        account_text=self.wd.find_element_by_id('id').text
        if account_text!=u'请输入账号':
            self.wd.find_element_by_id('id').clear()
        else:
            self.wd.find_element_by_id('YNTextView').click()
        alert_text=self.wd.switch_to_alert().text
        print alert_text
        #self.wd.get_screenshot_as_file(filename)
        #img=Image.open(filename)
        #result=pytesseract.image_to_string(img,lang='chi_sim')
        #print result
        #self.assertIn(u'请输入账号',result)
    #输入正确的账号密码，跳转至首页         
    def test_login(self):
        self.wd.find_element_by_id('id').send_keys('')
        self.wd.find_element_by_id('pwd').send_keys('')
        self.wd.find_element_by_id('YNTextView').click()
        sleep(3)
    #'保存密码，自动登录'checkbox   
    def test_checkbox(self):
        self.wd.find_element_by_id('checkbox').click()
        sleep(2)
        self.wd.find_element_by_id('checkbox').click()
        sleep(2)
class Clause(Imarketing_Longin):
    """《隐私条款》页面"""
     #点击《隐私条款》，是否跳转到《隐私条款》页面   
    def test_clause(self):
        """点击《隐私条款》，是否跳转到《隐私条款》页面"""
        self.wd.find_element_by_id('privacyPolicy').click()
        sleep(2)
        clause_title=self.wd.find_element_by_id('title').text
        self.assertEqual(clause_title,u'《隐私条款》')
    
    #《隐私条款》显示的内容是否正确
    def test_clause_content(self):
        """《隐私条款》显示的内容是否正确"""
        self.wd.find_element_by_id('privacyPolicy').click()
        sleep(2)
        content_text=self.wd.find_elements_by_class_name('android.view.View')[0].text
        #content_text=self.wd.find_element_by_accessibility_id('i畅销用户服务协议').text
        print content_text
        
    #点击《隐私条款》页面返回按钮，跳转至登录页面
    def test_clause_reback(self):
        """点击《隐私条款》页面返回按钮，跳转至登录页面"""
        self.wd.find_element_by_id('privacyPolicy').click()
        sleep(2)        
        self.wd.find_element_by_id('left').click()
        title=self.wd.find_element_by_id('title').text
        self.assertEqual(title, u'登录')        
        
        
if __name__=='__main__':
    case = unittest.TestSuite()
    case.addTest(Login_Features('test_clause_content'))
    runner=unittest.TextTestRunner(verbosity=2)
    #runner.run(case)
    #now=strftime('%Y-%m-%d %H-%M-%S')
    #fm='./'+now+'result.html'
    #fp=open(fm,'wb') 
    #runner=HTMLTestRunner(stream=fp,title='登陆页面页面样式测试报告',description='用例执行情况')
    #cases=unittest.TestLoader().loadTestsFromTestCase(Login_Page_Display)
    runner.run(case)
    #fp.close()
    
        