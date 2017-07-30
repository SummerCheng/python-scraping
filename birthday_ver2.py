#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.text import MIMEText

headers = {
    'Referer': 'http://bless.lyq.me/login/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Host': 'bless.lyq.me'
}
login_url ='http://bless.lyq.me/login/'
logined_url = 'http://bless.lyq.me'
session = requests.Session()

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


def login(email, password):

    driver = webdriver.Chrome('D:\Env\chromedriver.exe')
    # Go to the correct domain
    # driver.get("http://www.example.com")
    #
    # # Now set the cookie. This one's valid for the entire domain
    # cookie = {‘name’: ‘foo’, ‘value’: ‘bar’}
    # driver.add_cookie(cookie)
    #
    # # And now output all the available cookies for the current URL
    # driver.get_cookies()
    # driver.post(login_url, data=post_data, headers=headers)
    driver.get('http://bless.lyq.me/login/')
    elem = driver.find_element_by_id("email")
    elem.clear()
    elem.send_keys(email)
    elem.send_keys(Keys.RETURN)
    elem1 = driver.find_element_by_id("token")
    elem1.clear()
    elem1.send_keys(password)
    elem1.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)
    elem2 = driver.find_element_by_xpath("//a[@href='user_management/']")
    elem2.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    pageSource = driver.page_source
    bsObj1 = BeautifulSoup(pageSource)

    driver.switch_to.window(driver.window_handles[0])
    elem3 = driver.find_element_by_xpath("//a[@href='event_management/']")
    elem3.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[2])
    pageSource = driver.page_source
    bsObj2 = BeautifulSoup(pageSource)

    driver.close()
    return bsObj1,bsObj2

def get_email(bsObj):
    lst=[]
    for user_email in bsObj.findAll("option"):
        uname=user_email.get_text()
        umail=user_email.attrs['value']
        if user_email.attrs['value'] is not None:
            lst.append([uname,umail])
    return lst

def get_topiclst(bsObj):
    lst=[]
    today =time.strftime("%Y-%m-%d", time.localtime())
    for child in bsObj.find("table").thead.next_siblings:
        print(child)
        if child!="\n":
            a=[]
            for i in child.tr.td.next_siblings:
                if i!="\n":
                    a.append(i.get_text())
            if a[0]>today:
                lst.append(a)
            else:
                break
    return lst

def get_topic(lst):
    today=datetime.date.today()
    for event in lst:
        day=event[0].split('-')
        day1=datetime.date(int(day[0]),int(day[1]),int(day[2]))
        daydiff=(day1-today).days
        event.append(daydiff)
    return lst

def email(maillist,mailcontent,Topics):
    receiver = maillist[1]
    mail_host = "smtp.126.com"
    mail_user = "zxyatfkx@126.com"
    mail_pass = "12345678abc"
    mail_postfix = "126.com"


    sender = 'zxyatfkx@126.com'  # 发件人邮箱(最好写全, 不然会失败)
    content = "萌萌哒%s：\n"%(maillist[0])+mailcontent
    title = "生日祝福征集" # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receiver)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP()  # 启用SSL发信, 端口一般是465
        smtpObj.connect(mail_host)
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receiver, message.as_string())  # 发送
        smtpObj.quit()
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == "__main__":
    bs1,bs2=login(email='admin@bless', password='2013')
    # lst=get_email(bs1)
    topiclst=get_topiclst(bs2)
    topics=get_topic(topiclst)

    content=""
    for topic in topics:
        content+="%d天后（%s）是%s的生日\n"%(topic[5],topic[0],topic[2])
    content+="""
    如果还没有写祝福要记得写哦~地址：bless.lyq.me\n邮箱是收到邮件的这个，密码2013\n晚安~（时差党你什么也没有看到！）
    """
    lst=[['盐酸', 'sonnyhcl@outlook.com']]
    for user in lst:
        email(user, content,topics)



