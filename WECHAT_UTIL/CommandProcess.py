from WECHAT_UTIL.util.ChatroomFunctions import ChatroomFunctions
from WECHAT_UTIL.util.ContactFunctions import ContactFunctions
from WECHAT_UTIL.WechatMessage import WechatMessage
from WECHAT_UTIL.util.Functions import deepseek

def commandProcess(message: WechatMessage) -> bool:
    # 以后打算根据特定群聊名来选择特定回复的群聊
    content = message['content']

    if message['if_is_at_me']:
        pass

    return True