from WECHAT_UTIL.util.ChatroomFunctions import ChatroomFunctions
from WECHAT_UTIL.util.ContactFunctions import ContactFunctions
from WECHAT_UTIL.WechatMessage import WechatMessage,messageRestruct
from WECHAT_UTIL.CommandProcess import  commandProcess


def messageProcess(msg:dict) -> bool:
	"""
	处理信息的模块
	:param msg: 原始信息dict
	:return: 是否正确处理（但是没写不正确的~）
	"""
	message = messageRestruct(msg)

	name_chatroom = ""
	name_sender= ""
	name_sender_in_chatroom = ""
	if message['if_is_in_chatroom']:
		name_chatroom = "群聊 " + ChatroomFunctions.getChatroomName(message['sender'])
		name_sender_in_chatroom = ChatroomFunctions.getChatroomMemberNickname(message['sender'], message['sender_wechat_id'])
	else:
		name_sender = "私聊 " + ContactFunctions.get_contact_name(message['sender'])

	if message['if_is_send_by_myself']:
		if message['if_is_in_chatroom']:
			name_sender_in_chatroom = "me"
		else:
			name_sender += " me"

	msg_checks = {
		"emoji": "一个表情包",
		"img": "一个图片",
		"voicemsg": "一条语音信息",
		"videomsg": "一个视频文件",
		"refermsg": "一条回复信息（有待改进）",
		"<pat>": "发送了一个拍一拍",
		"appmsg": "一个链接/小程序"
	}

	sys_checks = {
		"dynacfg": "系统配置消息",
		"revokemsg": "撤回了一条消息",
		"pat": "拍了一下",
		"ChatSync": "正在同步消息",
		"<unreadchatlist>": "正在读取聊天信息"
	}

	if "<msg>" in message['content']: # 利用字典来进行消息的处理
		content = next((v for k, v in msg_checks.items() if k in message['content']), "一条特殊消息")
	elif "sysmsg" in message['content']:
		content = next((v for k, v in sys_checks.items() if k in message['content']), "其他系统消息")
	else:
		content = message['content']

	message_processed = (
		str(message['time']) + " "+
		(name_chatroom + " " + name_sender_in_chatroom + " " if message['if_is_in_chatroom'] else name_sender+" ") +
		("at了你" if message['if_is_at_me'] else "") +
		"发送了 "
	)
	message_processed += content
	print(message_processed)

	commandProcess(message)

	return True


if __name__ == "__main__":
	pass
