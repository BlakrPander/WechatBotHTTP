from WECHAT_UTIL.util.ChatroomFunctions import ChatroomFunctions
from WECHAT_UTIL.util.ContactFunctions import ContactFunctions
from WECHAT_UTIL.WechatMessage import WechatMessage
from WECHAT_UTIL.util.Functions import deepseek

def commandProcess(message: WechatMessage) -> bool:
    # �Ժ��������ض�Ⱥ������ѡ���ض��ظ���Ⱥ��
    content = message['content']

    if message['if_is_at_me']:
        pass

    return True