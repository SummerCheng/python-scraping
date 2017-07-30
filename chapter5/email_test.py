#! /usr/bin/env python  
# -*- coding: UTF-8 -*-  
import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
receivers = ['ruoyan.wei@outlook.com']
mail_host = "smtp.163.com"
mail_user = "lesleywry@163.com"
mail_pass = "nongyu521"
mail_postfix = "163.com"


sender = 'lesleywry@163.com'  # 发件人邮箱(最好写全, 不然会失败)



content = '晚安？感觉会有bug，大概发不出去!'
title = 'Python SMTP Mail Test'  # 邮件主题
message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    smtpObj.quit()
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)