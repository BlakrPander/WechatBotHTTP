import copy
from .WechatHttpApis import WECHAT_HTTP_APIS as APIS


# WechatBotHTTP api 参数模板
class WECHAT_HTTP_API_PARAM_TEMPLATES:
    __HTTP_API_PARAM_TEMPLATE = {
        # login check
        APIS.WECHAT_IS_LOGIN: {},


        # self info
        APIS.WECHAT_GET_SELF_INFO: {},


        # send message
        APIS.WECHAT_MSG_SEND_TEXT: {"wxid": "",
                                    "msg": ""},
        # wxids需要以`,`分隔，例如`wxid1,wxid2,wxid3`
        APIS.WECHAT_MSG_SEND_AT: {"chatroom_id":"",
                                  "wxids": "",
                                  "msg": "",
                                  "auto_nickname": 1},
        APIS.WECHAT_MSG_SEND_CARD: {"receiver":"",
                                    "shared_wxid":"",
                                    "nickname":""},
        APIS.WECHAT_MSG_SEND_IMAGE: {"receiver":"",
                                     "img_path":""},
        APIS.WECHAT_MSG_SEND_FILE: {"receiver":"",
                                    "file_path":""},
        APIS.WECHAT_MSG_SEND_ARTICLE: {"wxid":"",
                                       "title":"",
                                       "abstract":"",
                                       "url":"",
                                       "img_path":""},
        APIS.WECHAT_MSG_SEND_APP: {"wxid":"",
                                   "appid":""},


        # receive message
        APIS.WECHAT_MSG_START_HOOK: {"port": 10808},
        APIS.WECHAT_MSG_STOP_HOOK: {},
        APIS.WECHAT_MSG_START_IMAGE_HOOK: {"save_path":""},
        APIS.WECHAT_MSG_STOP_IMAGE_HOOK: {},
        APIS.WECHAT_MSG_START_VOICE_HOOK: {"save_path":""},
        APIS.WECHAT_MSG_STOP_VOICE_HOOK: {},


        # contact
        APIS.WECHAT_CONTACT_GET_LIST: {},
        APIS.WECHAT_CONTACT_CHECK_STATUS: {"wxid":""},
        APIS.WECHAT_CONTACT_DEL: {"wxid":""},
        APIS.WECHAT_CONTACT_SEARCH_BY_CACHE: {"wxid":""},
        APIS.WECHAT_CONTACT_SEARCH_BY_NET: {"keyword":""},
        APIS.WECHAT_CONTACT_ADD_BY_WXID: {"wxid":"",
                                          "msg":""},
        APIS.WECHAT_CONTACT_ADD_BY_V3: {"v3":"",
                                        "msg":"",
                                        "add_type": 0x6},
        APIS.WECHAT_CONTACT_ADD_BY_PUBLIC_ID: {"public_id":""},
        APIS.WECHAT_CONTACT_VERIFY_APPLY: {"v3":"",
                                           "v4":""},
        APIS.WECHAT_CONTACT_EDIT_REMARK: {"wxid":"",
                                          "remark":""},


        # chatroom
        APIS.WECHAT_CHATROOM_GET_MEMBER_LIST: {"chatroom_id":""},
        APIS.WECHAT_CHATROOM_GET_MEMBER_NICKNAME: {"chatroom_id":"",
                                                   "wxid":""},
        # wxids需要以`,`分隔，例如`wxid1,wxid2,wxid3`
        APIS.WECHAT_CHATROOM_DEL_MEMBER: {"chatroom_id":"",
                                          "wxids":""},
        # wxids需要以`,`分隔，例如`wxid1,wxid2,wxid3`
        APIS.WECHAT_CHATROOM_ADD_MEMBER: {"chatroom_id":"",
                                          "wxids":""},
        APIS.WECHAT_CHATROOM_SET_ANNOUNCEMENT: {"chatroom_id":"",
                                                "announcement":""},
        APIS.WECHAT_CHATROOM_SET_CHATROOM_NAME: {"chatroom_id":"",
                                                 "chatroom_name":""},
        APIS.WECHAT_CHATROOM_SET_SELF_NICKNAME: {"chatroom_id":"",
                                                 "nickname":""},


        # database
        APIS.WECHAT_DATABASE_GET_HANDLES: {},
        APIS.WECHAT_DATABASE_BACKUP: {"db_handle":0,
                                      "save_path":""},
        APIS.WECHAT_DATABASE_QUERY: {"db_handle":0,
                                     "sql":""},


        # version
        APIS.WECHAT_SET_VERSION: {"version": "3.7.0.30"},


        # log
        APIS.WECHAT_LOG_START_HOOK: {},
        APIS.WECHAT_LOG_STOP_HOOK: {},

        # browser
        APIS.WECHAT_BROWSER_OPEN_WITH_URL: {"url": "https://www.baidu.com/"},
        APIS.WECHAT_GET_PUBLIC_MSG: {"public_id": "","offset": ""},

        APIS.WECHAT_MSG_FORWARD_MESSAGE: {"wxid": "filehelper","msgid": 2 ** 64 - 1},
        APIS.WECHAT_GET_QRCODE_IMAGE: {},
        APIS.WECHAT_GET_A8KEY: {"url":""},
        APIS.WECHAT_MSG_SEND_XML: {"wxid":"filehelper","xml":"","img_path":""},
        APIS.WECHAT_LOGOUT: {},
        APIS.WECHAT_GET_TRANSFER: {"wxid":"","transcationid":"","transferid":""},
        APIS.WECHAT_MSG_SEND_EMOTION: {"wxid":"","img_path":""},
        APIS.WECHAT_GET_CDN: {"msgid":2 ** 64 - 1},
    }

    def get_http_template(self, api_number):
        try:
            return copy.deepcopy(self.__HTTP_API_PARAM_TEMPLATE[api_number])
        except KeyError:
            raise ValueError("There is no interface numbered %s." % api_number)