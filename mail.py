# coding 'utf-8'
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
import config


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = config.from_addr
password = config.password
to_addr = config.to_addr
smtp_server = config.smtp_server
print(from_addr)

# msg = MIMEText('你被淘汰啦！！！', 'plain', 'utf-8')
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('告诉你一个好消息！', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# def send_email(from_addr, to_addr, subject, password):
#     msg = MIMEText("邮件正文",'html','utf-8')
#     msg['From'] = u'<%s>' % from_addr
#     msg['To'] = u'<%s>' % to_addr
#     msg['Subject'] = subject

#     smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
#     smtp.set_debuglevel(1)
#     smtp.ehlo("smtp.163.com")
#     smtp.login(from_addr, password)
#     smtp.sendmail(from_addr, [to_addr], msg.as_string())

# if __name__ == "__main__":
#     # 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是邮箱密码
#     # 现在很多邮箱都需要先开启smtp才能这样发送邮件
#     send_email(u"13777830616@163.com",u"247482767@qq.com",u"测试",u"163sqm")