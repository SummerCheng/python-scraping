from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
#获取浏览器对象
driver = webdriver.PhantomJS(executable_path='D:/Env/phantomjs-2.1.1/bin/phantomjs')
#输入URL
driver.get("http://www.jd.com/")
#登录
inputElement=driver.find_element_by_xpath('//a[@href="javascript:login();"]').click()
inputElement=driver.find_element_by_id("loginname").send_keys("1588231")
inputElement=driver.find_element_by_id("nloginpwd").send_keys("ygq")
inputElement=driver.find_element_by_id("loginsubmit").click()

#搜索
inputElement=driver.find_element_by_id("key").send_keys(u"平底锅")
inputElement=driver.find_element_by_xpath('//div[@class="form"]//input[@class="button"]').click()
time.sleep(2)

inputElement=driver.find_element_by_xpath("//a[contains(@title,'跨年大促!自营厨具满4件免1件 截止到1月5日10点')]").click()
time.sleep(5)
#窗口切换
title=driver.title
handle=driver.get_window_position("京东网上商城-综合网购首选（JD.COM）-正品低价、品质保障、货到付款、配送及时、放心服务、轻松购物！")
for handle in driver.window_handles:
    driver.switch_to_window(handle)
    if handle in title:
        break
    time.sleep(2)

#增加购买数量并下单
inputElement=driver.find_element_by_xpath('//div/a[contains(.,"增加数量")]').click()
inputElement=driver.find_element_by_id("InitCartUrl").click()
#关闭
driver.quit()