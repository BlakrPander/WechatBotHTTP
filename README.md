# WechatBotHTTP

基于Windows Server平台，用Python写了接口的微信机器人，采用了ComWechatRobot框架里面的HTTP API接口调用
在配置好了环境之后，每次运行main.py即可。会自动启动微信的进程，同时修改版本号。


环境：
- 前置：[ComWechatRobot](https://github.com/ljc545w/ComWeChatRobot)
- 运行环境：
-   Windows Server 2022 数据中心版（x64)
-   Python 3.9.13（依赖在requirements.txt中）
-   Sublime Text（或者Notepad++）
-   [微信 3.7.0.30](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.7.0.30/WeChatSetup-3.7.0.30.exe)

使用配置：
- 安装好上述特定版本的微信
- 在WECHAT_UTIL/util/Functions/DeepSeek/configurations.json里，配置自己的apikey
- 在WECHAT_UTIL/util/chatroom.json里配置授权的群聊
- 运行WECHAT_UTIL/util/tmpfunctions/fixVersion.py
- 运行禁止微信更新.bat
- 运行main.py

开发计划：
- 想办法使用json/数据库的形式将聊天记录保存下来，然后在每次调用deepseek的时候，能够实现带聊天记录调用
- 打包一些常用的函数（自动通过好友申请等）
- 将ChatroomFunctions等这些分开来存储（函数按文件存储，方便后期修改与编辑）
- 多进程处理消息？


2025.3.26
- 添加了被at时自动接入deepseek
- 增加了写好的发消息、发at的函数接口


2025.3.24 
- 将消息处理模块重构，添加了WechatMessage类以更加方便的管理消息类的变量
- 修复了被at时不提示”at了你“的问题
- 将is_at_me函数放到了ChatroomFunctions类中，更方便后期使用管理


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
