#encoding:utf-8
from appium import webdriver

global wd 
def star_up_appium():
    desired_caps={}
    desired_caps['platformName']='Android'
    desired_caps['platformVesion']='6.0'
    desired_caps['deviceName']='HUAWEI MT7-TL00'
    desired_caps['appPackage']='com.bcc.bestselling'
    desired_caps['appActivity']='com.bcc.bestselling.activity.LogoActivity'
    desired_caps['unicodeKeyboard']='True'
    desired_caps['resetKeyboard']='True'

    wd=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    sleep(3)
    return wd 

def stop_appium():
    return wd.quit()