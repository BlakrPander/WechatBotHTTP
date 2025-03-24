from .WechatHttpApiUtils import WECHAT_HTTP_API_OP as OP
from .WechatHttpApiUtils import WECHAT_HTTP_APIS as APIS
import json
import re

post_wechat_http_api = OP.post_wechat_http_api
get_wechat_http_api = OP.get_wechat_http_api

class ChatroomFunctions:

    @staticmethod
    def get_chatroom_member_nickname(chatroom:str, sender_wechat_id:str, port = 8000) -> str :
        """
        根据群聊id以及微信id，获取在群聊中特定群员的名称
        :param chatroom: 从原始消息中获到的群聊id
        :param senderWechatId: 从原始消息中获得的微信id
        :param port: http通信端口（默认为8000）
        """
        nickname = ''
        data = {
            "chatroom_id":chatroom,
            "wxid":sender_wechat_id
        }
        res = post_wechat_http_api(APIS.WECHAT_CHATROOM_GET_MEMBER_NICKNAME, data = data, port = port)
        nickname = res['nickname']
        return nickname


    @staticmethod
    def get_chatroom_name(chatroom:str, port = 8000) -> str :
        """
        根据群聊id获取群聊名称
        :param chatroom: 从原始消息种获取到来的群聊id
        :param port: http通信端口（默认为8000）
        """
        data={
            "wxid":chatroom
        }
        res = post_wechat_http_api(APIS.WECHAT_CONTACT_SEARCH_BY_CACHE, data = data, port = port)
        chatroom_name=res['data']['wxNickName']
        return chatroom_name


    @staticmethod
    def is_at_me(extrainfo: str,my_wxid: str) -> bool:
        """
        检查是否被@（支持单独@和多人@）
        :param extrainfo: JSON中的extrainfo字段
        :param my_wxid: 用户微信ID
        """
        pattern=r"<atuserlist><!\[CDATA\[(.*?)\]\]></atuserlist>"
        match=re.search(pattern,extrainfo)
        if not match: return False
        user_list=[uid.strip() for uid in match.group(1).split(",") if uid.strip()]
        return my_wxid in user_list