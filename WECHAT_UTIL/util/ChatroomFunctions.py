from .WechatHttpApiUtils import WECHAT_HTTP_API_OP as OP
from .WechatHttpApiUtils import WECHAT_HTTP_APIS as APIS
import json

post_wechat_http_api = OP.post_wechat_http_api
get_wechat_hhtp_api = OP.get_wechat_http_api

class ChatroomFunctions:

    @staticmethod
    def get_chatroom_member_nickname(chatroom:str, senderWechatId:str, port = 8000) -> str :
        nickname = ''
        data = {
            "chatroom_id":chatroom,
            "wxid":senderWechatId
        }
        res = post_wechat_http_api(APIS.WECHAT_CHATROOM_GET_MEMBER_NICKNAME, data = data, port = port)
        nickname = res['nickname']
        return nickname

    @staticmethod
    def get_chatroom_name(chatroom:str, port = 8000) -> str :
        data={
            "wxid":chatroom
        }
        res = post_wechat_http_api(APIS.WECHAT_CONTACT_SEARCH_BY_CACHE, data = data, port = port)
        chatroom_name=res['data']['wxNickName']
        return chatroom_name