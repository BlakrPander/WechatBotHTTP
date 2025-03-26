from .WechatHttpApiUtils import WECHAT_HTTP_API_OP as OP
from .WechatHttpApiUtils import WECHAT_HTTP_APIS as APIS

post_wechat_http_api = OP.post_wechat_http_api
get_wechat_http_api = OP.get_wechat_http_api

class UniversalFunctions:
    @staticmethod
    def sendMessage(target_id: str, content: str, port=8000) -> bool:
        """
        向指定微信id发送消息（群聊和个人通用，用群聊id则向群聊发送消息，用个人微信id则向个人发送消息）
        :param target_id: 目标id
        :param content: 要发送的内容
        :param port: http通信端口（默认为8000）
        :return: 是否发送成功（待改进）
        """
        data = {
            "wxid": target_id,
            "msg": content
        }
        res = post_wechat_http_api(APIS.WECHAT_MSG_SEND_TEXT, data = data, port = port)
        if res['result']=="OK":
            return True
        else:
            return False
