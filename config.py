# Send mail
# e.g. send from 00000000@163.com to 00000000@qq.com
SMTP_HOST = ''  # SMTP服务器地址，如 'smtp.qq.com', 'smtp.163.com', 'mail.ustc.edu.cn'
SMTP_PORT = 465  # SMTP端口，通常为465（SSL）或587（TLS）
SMTP_USERNAME = ''  # SMTP用户名（通常是邮箱地址）
SMTP_PASSWORD = ''  # SMTP密码（部分邮箱需要填写授权码而不是登录密码）
SENDER = ''  # 发件人邮箱地址
RECEIVER = ''  # 收件人邮箱地址

# Period
PERIOD = 10  # 扫描间隔时间（分钟），推荐 10 ~ 60，十分不推荐设置过低

# Educational administration system information
STUDENT_ID = ''  # 学号
PASSWORD = ''  # 教务系统密码

# Retry MAX_TIME times on error
MAX_TIME = 10