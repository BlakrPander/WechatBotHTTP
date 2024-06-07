from .WechatHttpApiUtils import WECHAT_HTTP_API_OP as OP
from .WechatHttpApiUtils import WECHAT_HTTP_APIS as APIS
import json

post_wechat_http_api = OP.post_wechat_http_api
get_wechat_http_api = OP.get_wechat_http_api

class ContactFunctions:
    @staticmethod
    def get_contact_name(wechatId:str, port = 8000) ->str:
        data={
            "wxid":wechatId
        }
        res = post_wechat_http_api(APIS.WECHAT_CONTACT_SEARCH_BY_CACHE, data = data, port = port)
        resdata = res['data']
        if type(resdata) == str:
            contact_name = resdata
        else:
            contact_name = res['data']['wxNickName'] 
        return contact_name
