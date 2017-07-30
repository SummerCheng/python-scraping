#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

import smtplib
from email.mime.text import MIMEText

mailto_list=['zxyatfkx@126.com']
mail_host="smtp.163.com"
mail_user="lesleywry@163.com"
mail_pass="nongyu521"
mail_postfix="163.com"

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "lesleywry@163.com"
msg['To'] = "webmaster@pythonscraping.com"

s = smtplib.SMTP('smtp.163.com')
s.send_message(msg)
s.quit()