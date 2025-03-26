from .WechatHttpApiUtils import WECHAT_HTTP_API_OP as OP
from .WechatHttpApiUtils import WECHAT_HTTP_APIS as APIS
import json
import re
import os
from pathlib import Path

post_wechat_http_api = OP.post_wechat_http_api
get_wechat_http_api = OP.get_wechat_http_api


class ChatroomFunctions:
    @staticmethod
    def sendAtMessage(target_chatroom_id: str, target_wechat_id: str, content: str, port=8000) -> bool:
        """
        向指定微信群聊发送at指定消息
        :param target_chatroom_id: 目标群聊
        :param target_wechat_id: 目标id
        :param content: 要发送的内容
        :param port: http通信端口（默认为8000）
        :return: 是否发送成功（待改进）
        """
        data = {
            "chatroom_id": target_chatroom_id,
            "wxids": target_wechat_id,
            "msg": content,
            "auto_nickname": 1
        }
        res = post_wechat_http_api(APIS.WECHAT_MSG_SEND_AT, data = data, port = port)
        # print(res)
        if res['result']=="OK":
            return True
        else:
            return False


    @staticmethod
    def getChatroomMemberNickname(chatroom_id: str, sender_wechat_id: str, port=8000) -> str:
        """
        根据群聊id以及微信id，获取在群聊中特定群员的名称
        :param chatroom_id: 从原始消息中获到的群聊id
        :param senderWechatId: 从原始消息中获得的微信id
        :param port: http通信端口（默认为8000）
        """
        data = {
            "chatroom_id": chatroom_id,
            "wxid": sender_wechat_id
        }
        res = post_wechat_http_api(APIS.WECHAT_CHATROOM_GET_MEMBER_NICKNAME, data=data, port=port)
        nickname = res['nickname']
        return nickname

    @staticmethod
    def getChatroomName(chatroom_id: str, port=8000) -> str:
        """
        根据群聊id获取群聊名称
        :param chatroom_id: 从原始消息种获取到来的群聊id
        :param port: http通信端口（默认为8000）
        """
        data = {
            "wxid": chatroom_id
        }
        res = post_wechat_http_api(APIS.WECHAT_CONTACT_SEARCH_BY_CACHE, data=data, port=port)
        chatroom_name = res['data']['wxNickName']
        return chatroom_name

    @staticmethod
    def is_at_me(extrainfo: str, my_wxid: str) -> bool:
        """
        检查是否被@（支持单独@和多人@）
        :param extrainfo: JSON中的extrainfo字段
        :param my_wxid: 用户微信ID'
        :return: 是否被at
        """
        pattern = r"<atuserlist>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</atuserlist>"
        match = re.search(pattern, extrainfo)
        if not match:
            return False
        user_list = [uid.strip() for uid in match.group(1).split(",") if uid.strip()]
        return my_wxid in user_list

    @staticmethod
    def checkIfChatroomInApprovedList(chatroom_id: str, chatroom_list_filepath=None) -> bool:
        """
        用于检查群聊id是否在被允许的群聊名单中
        :param chatroom_id: 要查询的群聊id
        :param chatroom_list_filepath: 允许的群聊名单文件的存储路径，默认为同路径下
        :return: True为存在 False为不存在
        """
        module_dir = os.path.dirname(os.path.abspath(__file__))

        # 如果未指定路径，使用模块目录下的chatroom.json
        if chatroom_list_filepath is None:
            chatroom_list_filepath = os.path.join(module_dir, 'chatroom.json')

        with open(chatroom_list_filepath, 'r') as chatroom_file:
            chatroom_list: list = json.load(chatroom_file)
        return chatroom_id in chatroom_list

    @staticmethod
    def addChatroomInApprovedList(chatroom_id: str, chatroom_list_filepath=None) -> bool:
        """
        在允许的群聊列表中增加新的群聊id
        :param chatroom_id: 要增加的群聊id
        :param chatroom_list_filepath: 允许的群聊名单的文件存储位置 默认为同目录
        :return: True为添加成功 False为添加失败
        """
        module_dir = os.path.dirname(os.path.abspath(__file__))

        # 如果未指定路径，使用模块目录下的chatroom.json
        if chatroom_list_filepath is None:
            chatroom_list_filepath = os.path.join(module_dir, 'chatroom.json')

        with open(chatroom_list_filepath, 'r') as chatroom_file:
            chatroom_list: list = json.load(chatroom_file)
        if not chatroom_id in chatroom_list:
            chatroom_list.append(chatroom_id)
        else:
            return False

        temp_path = Path(chatroom_list_filepath).with_suffix('.tmp')
        try:
            with open(temp_path, 'w', encoding='utf-8') as f:
                json.dump(chatroom_list, f, ensure_ascii=False, indent=2)

            temp_path.replace(Path(chatroom_list_filepath))
            return True
        except Exception as e:
            # 清理临时文件
            if temp_path.exists():
                temp_path.unlink()
            raise False

    @staticmethod
    def deleteChatroomInApprovedList(chatroom_id: str, chatroom_list_filepath=None) -> bool:
        """
        在允许的群聊列表中删除群聊id
        :param chatroom_id: 要删除的群聊id
        :param chatroom_list_filepath: 允许的群聊名单的文件存储位置 默认为同目录
        :return: True为添加成功 False为添加失败
        """
        module_dir = os.path.dirname(os.path.abspath(__file__))

        # 如果未指定路径，使用模块目录下的chatroom.json
        if chatroom_list_filepath is None:
            chatroom_list_filepath = os.path.join(module_dir, 'chatroom.json')

        with open(chatroom_list_filepath, 'r') as chatroom_file:
            chatroom_list: list = json.load(chatroom_file)
        if not chatroom_id in chatroom_list:
            chatroom_list.remove(chatroom_id)
        else:
            return False

        temp_path = Path(chatroom_list_filepath).with_suffix('.tmp')
        try:
            with open(temp_path, 'w', encoding='utf-8') as f:
                json.dump(chatroom_list, f, ensure_ascii=False, indent=2)

            temp_path.replace(Path(chatroom_list_filepath))
            return True
        except Exception as e:
            if temp_path.exists():
                temp_path.unlink()
            raise False


if __name__ == "__main__":
    print(ChatroomFunctions.checkIfChatroomInApprovedList("chatroom@1234"))
    print(ChatroomFunctions.checkIfChatroomInApprovedList("chatroom@666"))
    print(ChatroomFunctions.addChatroomInApprovedList("chatroom@666"))
    print(ChatroomFunctions.checkIfChatroomInApprovedList("chatroom@666"))
