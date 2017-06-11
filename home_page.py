#encoding:utf-8
import unittest
from appium import webdriver
from time import sleep,strftime
import common
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#from ddt import ddt,data,unpack



class Home_Page_mask(unittest.TestCase):
    def setUp(self):
        self.wd=common.star_up_appium()
        #判断当前页面是否为首页，是：跳转至面膜详情页面；否，先登陆
        if self.wd.current_activity=='.activity.MainActivity':
            elemens=self.wd.find_elements_by_id('image')[0].click()#点击面膜按钮
            sleep(3)#等待3秒钟            
            
        else:
            self.wd.find_element_by_id('id').send_keys('hdy123') #输入账号
            self.wd.find_element_by_id('pwd').send_keys('111111')#输入密码
            self.wd.find_element_by_id('YNTextView').click() #点击‘登陆’
            sleep(3)#等待3秒钟 
            elemens=self.wd.find_elements_by_id('image')[0].click()#点击面膜按钮
            
            
    def test_search(self):
        """测试点击'查询'按钮，页面跳转至品牌搜索页面"""
        self.wd.find_element_by_id('search').click()#点击查询按钮
        sleep(2)
        if self.wd.find_elements_by_id('shop')[0].text=='Tmall Mask':
            print '页面跳转正确'
        else:
            print '页面跳转不成功'
            
    #----------------------------------------------------------------------
    def test_return_button(self):
        """验证'返回'按钮是否有效"""
        self.wd.find_element_by_id('search').click()#点击查询按钮
        self.wd.find_element_by_id('leftImageView').click()#点击‘<’按钮
        #以返回的页面是否显示查询按钮来判断返回的页面是否正确
        if self.wd.find_element_by_id('search').is_displayed():
            print '返回面膜详情页面'
        
        else:
            print '未返回面膜详情页面'
        
    #----------------------------------------------------------------------
    def test_collect_search_accurate(self):
        """精确查询，唯一结果"""
        self.wd.find_element_by_id('search').click()#点击查询按钮
        self.wd.find_element_by_id('collect_search').send_keys(u'贝亦美')#输入搜索关键字
        self.wd.find_element_by_id('searchButton').click()#点击‘搜索’按钮
        result=self.wd.find_elements_by_class_name('android.widget.TextView').text
        if self.assertIn(keywords,result):
            print '查询结果与关键词匹配'
        else:
            print '查询结果与关键字不匹配'
            
    #----------------------------------------------------------------------
    def test_collect_search_blurry(self):
        """模糊查询"""
        self.wd.find_element_by_id('search').click()#点击查询按钮
        self.wd.find_element_by_id('collect_search').send_keys(u'七水')#输入搜索关键字
        self.wd.find_element_by_id('searchButton').click()#点击‘搜索’按钮
        result=self.wd.find_elements_by_class_name(android.widget.TextView).text
        if self.assertIn(keywords,result):
            print '查询结果与关键词匹配'
        else:
            print '查询结果与关键字不匹配'        
        
            
    #----------------------------------------------------------------------
    def test_seach_button(self):
        """为输入关键字，点击‘搜索’按钮"""
        self.wd.find_element_by_id('search').click()#点击查询按钮       
        self.wd.find_element_by_id('searchButton').click()#点击‘搜索’按钮
        sleep(2)
        print '无法获取弹框信息'
                    
    def tearDown(self):
        self.wd.quit()
        
if __name__=='__main__':
    case=unittest.TestSuite()
    case.addTest(Home_Page_mask('test_seach_button'))
    #caserun=unittest.TextTestRunner(verbosity=2)
    
    now=strftime("%Y-%m-%d %H-%M-%S")
    filename='./'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title=u'品牌搜索页面测试报告',description=u'用例执行情况：')
    runner.run(case)
    fp.close()