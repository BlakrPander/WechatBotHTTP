from WECHAT_UTIL.util.ChatroomFunctions import ChatroomFunctions
from WECHAT_UTIL.util.ContactFunctions import ContactFunctions
from WECHAT_UTIL.util.UniversalFunctions import UniversalFunctions
from WECHAT_UTIL.WechatMessage import WechatMessage
from WECHAT_UTIL.util.Functions.DeepSeek.DeepSeekClient import DeepSeekClient

def commandProcess(message: WechatMessage) -> bool:
    # 以后打算根据特定群聊名来选择特定回复的群聊
    content = message['content']
    sender = message['sender']

    if message['if_is_in_chatroom']:
        if ChatroomFunctions.checkIfChatroomInApprovedList(sender): # 是被允许提供服务的群聊
            if message['if_is_at_me']:
                ChatroomFunctions.sendAtMessage(
                    target_chatroom_id = sender,
                    target_wechat_id = message['sender_wechat_id'],
                    content = DeepSeekClient.generateReply(content)
                )
                pass
            else:
                # 接下来写随机回复 带历史记录回复以及私聊回复
                pass #其余群聊指令逻辑匹配处理






    return True


