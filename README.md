# USTC Grade Notification

中科大教务系统成绩自动检测与邮件通知脚本

## 原项目

本项目基于 [yusanshi/USTC-grade-notification](https://github.com/yusanshi/USTC-grade-notification) 进行更新和改进。

## 功能

- 自动检测中科大教务系统成绩更新
- 发现新成绩时发送邮件通知
- 支持开机自启动
- 启动时弹窗提示脚本运行状态

## 环境要求

- Python 3.8+
- Windows 系统（开机自启动功能基于 Windows）

## 安装

```bash
pip install pyustc pywin32 winshell
```

## 配置

编辑 `config.py` 文件，填写以下配置信息：

```python
# 邮件配置
SMTP_HOST = 'smtp.qq.com'          # SMTP服务器地址
SMTP_PORT = 465                     # SMTP端口
SMTP_USERNAME = 'your_email@qq.com' # SMTP用户名
SMTP_PASSWORD = 'your_password'     # SMTP密码/授权码
SENDER = 'your_email@qq.com'        # 发件人邮箱
RECEIVER = 'target_email@qq.com'    # 收件人邮箱

# 扫描间隔（分钟），推荐 10-60
PERIOD = 10

# 教务系统信息
STUDENT_ID = 'PB20200000'           # 学号
PASSWORD = 'your_password'          # 教务系统密码
```

**邮箱授权码获取方法：**

- **QQ邮箱**: 设置 -> 账户 -> 开启POP3/SMTP服务 -> 获取授权码
- **163邮箱**: 设置 -> POP3/SMTP/IMAP -> 开启SMTP服务 -> 获取授权码
- **科大邮箱**: 需要在邮箱设置获取专用密码

## 使用

### 手动运行

```bash
python main.py
```

或者双击 `run.bat` 文件。

### 开机自启动

运行以下命令设置开机自启动：

```bash
python setup_auto_start.py
```

取消开机自启动：

```bash
python setup_auto_start.py disable
```

## 文件结构

```
USTC-grade-notification/
├── config.py          # 配置文件
├── main.py            # 主程序入口
├── get_grade.py       # 成绩获取模块
├── login.py           # 登录模块
├── send_mail.py       # 邮件发送模块
├── run.bat            # 启动脚本
├── setup_auto_start.py # 开机自启动配置
├── .gitignore         # Git忽略文件
└── README.md          # 项目说明
```

## 工作原理

1. 使用 `pyustc` 库登录中科大统一身份认证系统
2. 进入教务系统获取当前所有成绩
3. 每隔指定时间（默认10分钟）重新获取成绩
4. 对比新旧成绩，发现新增成绩时发送邮件通知
5. 支持异常重试机制（默认10次）

## 注意事项

1. 请勿将 `config.py` 文件提交到代码仓库，避免泄露个人信息
2. 建议将扫描间隔设置为10分钟以上，避免给教务系统造成压力
3. 脚本运行期间需要保持电脑开机
4. 如果教务系统登录方式发生变化，可能需要更新代码

## 许可证

本项目采用 MIT License 许可证。

原项目作者：yusanshi  
原项目地址：https://github.com/yusanshi/USTC-grade-notification
