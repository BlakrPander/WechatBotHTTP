from ..WECHAT_UTIL import WECHAT_HTTP_API_OP
from ..WECHAT_UTIL import WECHAT_HTTP_APIS as APIS
import json


post_wechat_http_api = WECHAT_HTTP_API_OP().post_wechat_http_api
get_wechat_hhtp_api = WECHAT_HTTP_API_OP().get_wechat_http_api


def test_send_msg(test_port):
    post_wechat_http_api(APIS.WECHAT_LOG_START_HOOK,port = test_port)
    if post_wechat_http_api(APIS.WECHAT_IS_LOGIN,port = test_port)["is_login"] == 1:
        print(post_wechat_http_api(APIS.WECHAT_GET_SELF_INFO,port = test_port))

        data = {"wxid":"filehelper","msg":"hello WechatBotHTTP"}
        post_wechat_http_api(APIS.WECHAT_MSG_SEND_TEXT,data = data,port = test_port)

        data = {"receiver":'filehelper',"shared_wxid":"filehelper","nickname":"文件传输助手"}
        post_wechat_http_api(APIS.WECHAT_MSG_SEND_CARD,data = data,port = test_port)

        data = {"receiver":'filehelper',"img_path":r"D:\VS2019C++\MyWeChatRobot\test\测试图片.png"}
        post_wechat_http_api(APIS.WECHAT_MSG_SEND_IMAGE,data = data,port = test_port)

        data = {"receiver":'filehelper',"file_path":r"D:\VS2019C++\MyWeChatRobot\test\测试文件"}
        post_wechat_http_api(APIS.WECHAT_MSG_SEND_FILE,data = data,port = test_port)

        data = {"wxid":'filehelper',
                "title":"百度",
                "abstract":"百度一下，你就知道",
                "url":"https://www.baidu.com/",
                "img_path":""}
        post_wechat_http_api(APIS.WECHAT_MSG_SEND_ARTICLE,data = data,port = test_port)
        print(post_wechat_http_api(APIS.WECHAT_CONTACT_GET_LIST,port = test_port))
        data = {"wxid":"filehelper"}
        print(post_wechat_http_api(APIS.WECHAT_CONTACT_CHECK_STATUS,data = data,port = test_port))
    post_wechat_http_api(APIS.WECHAT_LOG_STOP_HOOK,port = test_port)

def test_get_public_msg(test_port,public_id):
    import time
    param = {"public_id": public_id,"offset": ""}
    data = post_wechat_http_api(APIS.WECHAT_GET_PUBLIC_MSG,test_port,param)
    msg_list = json.loads(data['msg'])['MsgList']
    next_offset = msg_list['PagingInfo']['Offset']
    for msg in msg_list['Msg']:
        detail_info = msg['AppMsg']['DetailInfo']
        for info in detail_info:
            Title = info['Title']
            Digest = info['Digest']
            ContentUrl = info['ContentUrl']
            a8key_dict = post_wechat_http_api(APIS.WECHAT_GET_A8KEY,
                                              port = test_port,
                                              data = {"url":ContentUrl})
            print(a8key_dict)
            post_wechat_http_api(APIS.WECHAT_BROWSER_OPEN_WITH_URL,
                                 test_port,
                                 {"url":ContentUrl}
                                 )
            time.sleep(3)
            break
        break

def test_get_chatroom_list_from_db(test_port):
    dbs = post_wechat_http_api(APIS.WECHAT_DATABASE_GET_HANDLES,port = test_port)
    db_handle = [i for i in dbs['data'] if i['db_name'] == 'MicroMsg.db'][0]['handle']
    sql = "select UserName,Alias,EncryptUserName,Type,VerifyFlag,Remark,NickName,ChatRoomType,ExtraBuf from Contact where Type=2;"
    data = {"db_handle":db_handle,"sql":sql}
    res = post_wechat_http_api(APIS.WECHAT_DATABASE_QUERY,data = data,port = test_port)
    return res['data']