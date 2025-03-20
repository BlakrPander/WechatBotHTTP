# WechatBotHTTP

采用ComWechatRobot框架的机器人，采用了HTTP的API接口调用

环境：
- 前置：[ComWechatRobot](https://github.com/ljc545w/ComWeChatRobot)
- 运行环境：
-   Windows Server 2022 数据中心版（x64)
-   Python 3.9.13
-   Sublime Text
-   [微信 3.7.0.30](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.7.0.30/WeChatSetup-3.7.0.30.exe)

使用时，需要先安装好上述特定版本的微信，然后直接运行main.py即可

2025.3.20
中间或多或少做了一点git的规范，但是都没记录，今天重新将项目部署，特别记录一下
将项目部署在虚拟机里，方便后续快速在服务器上进行部署

2024.6.6：
更新：
1. 将原本一个.py中的文件分成了几份，方便开发
2. 封装了一些常用函数：获取群聊名称、群聊成员名称、好友列表名称等

预期开发目标：
1. 本地再写一个日志文件，能够将微信接受下来的消息内容等进行记录
2. 完善消息的识别，包括：回复信息，文件信息，小程序/链接信息等的识别与关键信息的输出
3. 增加指令内容的识别（可以用之前的字符串匹配的方式，然后一些之前写过的函数也可以拿过来用）
