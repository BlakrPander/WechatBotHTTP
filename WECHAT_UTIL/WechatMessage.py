from typing import TypedDict, Optional
from WECHAT_UTIL.util.ChatroomFunctions import ChatroomFunctions


class WechatMessage(TypedDict):
	"""
	规格化之后的微信消息类
	"""
	# metadata:
	extrainfo:Optional[str]
	id:Optional[str]
	type:Optional[str]
	content:Optional[str]

	# sender
	sender:Optional[str] # 当在群聊里时 sender内容为群聊id 当为私聊时 sender为个人微信id
	self_wechat_id:Optional[str]
	sender_wechat_id:Optional[str]

	# file
	file_path:Optional[str]
	thumb_path:Optional[str]
	sign:Optional[str]

	# time
	time:Optional[int]
	time_stamp:Optional[int]

	# flags
	if_is_send_by_phone:Optional[bool]
	if_is_send_by_myself:Optional[bool]
	if_is_at_me:Optional[bool]
	if_is_in_chatroom:Optional[bool]

	# pid
	process_id:Optional[int]


def messageRestruct(msg: dict) -> WechatMessage:
	"""
	将原始信息转化为微信消息类
	:param msg: 原始消息
	:return: 转换好的微信消息类
	"""
	restructed_message:WechatMessage = {
		"extrainfo": msg.get('extrainfo',None),
		"id": msg.get('msgid',None),
		"type": msg.get('type',None),
		"content": msg.get('message',None),

		"sender": msg.get('sender',None),
		"self_wechat_id": msg.get('self',None),
		"sender_wechat_id": msg.get('wxid',None),

		"file_path": msg.get('filepath',None),
		"sign": msg.get('sign',None),
		"thumb_path": msg.get('thumb_path',None),

		"time": msg.get('time',None),
		"time_stamp": msg.get('timestamp',None),

		"if_is_send_by_phone": msg.get('isSendByPhone',None),
		"if_is_send_by_myself": msg.get('isSendMsg',None),
		"if_is_at_me": ChatroomFunctions.is_at_me(
			extrainfo = msg.get('extrainfo'),
			my_wxid = msg.get('self')
		),
		"if_is_in_chatroom": (True if "chatroom" in msg.get('sender') else False),

		"wechat_process_id": msg.get('pid',None)
	}
	return restructed_message
